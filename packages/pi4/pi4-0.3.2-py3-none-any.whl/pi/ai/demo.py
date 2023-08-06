import sys
import os.path
from pathlib import Path
from datetime import datetime
from tkinter import PhotoImage,Radiobutton,font
from ttkbootstrap.toast import ToastNotification
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.icons import Emoji

import cv2
from PIL import Image, ImageTk

import webbrowser
from random import choice

if __package__:
    from ..gui.toastx import ToastNotificationX
    from ..gui.file_search_frame import FileSearchFrame
    from . import emo
    from .blur import overlay_image
    from .tflite.classification import Classifier, RopClassifier, FlowerClassifier
    from ..gui import CollapsableFrame
else:
    GUI_DIR = os.path.dirname (os.path.dirname(__file__)) + '/gui' 
    if GUI_DIR not in sys.path:
        sys.path.append(GUI_DIR)

    AI_DIR = os.path.dirname (os.path.dirname(__file__)) + '/ai' 
    if AI_DIR not in sys.path:
        sys.path.append(AI_DIR)
        
    PI_DIR = os.path.dirname (os.path.dirname(__file__)) 
    if PI_DIR not in sys.path:
        sys.path.append(PI_DIR)

    from toastx import ToastNotificationX
    from file_search_frame import FileSearchFrame
    import emo
    from blur import overlay_image
    from tflite.classification import Classifier, RopClassifier, FlowerClassifier
    from gui import CollapsableFrame

cap = cv2.VideoCapture(0)
INTERVAL = 100 # ms
SAVE_DIR = 'ocam_captures/'
PADDING = 9
DEFAULT_WINSIZE = '500x400'
ENABLE_FULLSCREEN = True # NOTE: messagebox can be hided by fullscreen windows. 
PATH = Path(__file__).parent

def get_timestamp():   

    now = datetime.now() # current date and time

    dt = now.strftime("%Y%m%d%H%M%S")
    return dt

class MainApp(ttk.Frame):

    def __init__(self, master):

        super().__init__(master)
        self.pack(fill=BOTH, expand=YES)
        
        self.images = [
            PhotoImage(
                name='mount', 
                file=PATH / 'mount.png'),
        ]
        
        # left panel
        left_panel = ttk.Frame(self, style='bg.TFrame')
        left_panel.pack(side=LEFT, fill=Y)

        cf1 = CollapsableFrame(left_panel)
        cf1.pack(fill=X, pady=1)

        ## container
        frm1 = ttk.Frame(cf1, padding=5)
        frm1.columnconfigure(1, weight=1)
        cf1.add(
            child=frm1, 
            title='AI', 
            bootstyle=SECONDARY)

        self.create_buttonbox(frm1)

        # right panel
        right_panel = ttk.Frame(self, padding=(2, 1))
        right_panel.pack(side=RIGHT, fill=BOTH, expand=YES)
        
        # img_path = Path(__file__).parent / 'assets/mp_background.png'
        # self.demo_media = ttk.PhotoImage(file=img_path)
        self.media = ttk.Label(right_panel) # , image=self.demo_media)
        self.media.pack(fill=BOTH, expand=YES)
        self.print_camera_properties()
        
        self.UpdateImage(INTERVAL)

    def print_camera_properties(self):

        properties = []
        for name in dir(cv2):
            if name.startswith('CAP_PROP'):
                value = getattr(cv2, name)
                properties.append((value, name))
                
        # it will sort by values
        # originally it is sorted by names
        properties = sorted(properties)

        if (len(properties) > 0):
            print('\n------- Camera Properties ------\n')
            for value, name in properties:
                print(f' {value:5} | cv2.{name}')

    def create_buttonbox(self, container = None):
        """Create buttonbox with media controls"""

        if container is None:
            container = ttk.Frame(self)
            container.pack(fill=X, expand=YES)

        ttk.Style().configure('TButton', font="-size 14")
        
        f = font.Font(size=20)
        btn = ttk.Button(
            master=container,
            text = Emoji.get('CAMERA WITH FLASH'),
            padding=PADDING,
            command= self.capture_image
        )
        # btn['font'] = f
        # btn.pack(side=LEFT, fill=X, expand=YES)  
        btn.grid(row=0, column=0, sticky=N+S+E+W)

        btn = ttk.Button(
            master=container,
            text=Emoji.get('open file folder'),
            # image='folder',
            padding=PADDING,
            command= self.open_save_folder
        )
        # btn['font'] = f
        # btn.pack(side=LEFT, fill=X, expand=YES)          
        btn.grid(row=1, column=0, sticky=N+S+E+W)

        lbl = ttk.Label(master=container,
        text='Select an AI task:', padding = PADDING, font=('Times', 15))
        lbl.grid(row=2, column=0, sticky=N+S+E+W)

        self.task = ttk.StringVar(self, "blur") # any of 'emotion', 'C1000', 'flower', 'rop', 'coco'. but coco is slow.
        
        # Dictionary to create multiple buttons
        values = {"Blur Detecction" : "blur",
                "Emotion Detection" : "emotion",
                "1000-Classification" : "C1000",
                "Flower Classfication" : "flower",
                "ROP Classificaiton" : "rop"}
        
        # Loop is used to create multiple Radiobuttons
        # rather than creating each button separately
        rid = 3
        for (text, value) in values.items():
            Radiobutton(container, text = text, variable = self.task, value = value,
            height = 1,
            font=('Times', 15)).grid(row=rid, column=0, sticky=N+S+E+W)   
            rid = rid + 1 
        
        btn = ttk.Button(
            master=container,
            text=Emoji.get('LOWER LEFT PAINTBRUSH'),
            padding=PADDING,
            command = self.change_style
        )
        # btn['font'] = f
        # btn.pack(side=LEFT, fill=X, expand=YES)  
        btn.grid(row=10, column=0, sticky=N+S+E+W) 

        btn = ttk.Button(
            master=container,
            text=Emoji.get('NEGATIVE SQUARED CROSS MARK'),
            padding=PADDING,
            command = self.quit # destroy is not enough
        )
        # btn['font'] = f
        # btn.pack(side=LEFT, fill=X, expand=YES) 
        btn.grid(row=11, column=0, sticky=N+S+E+W)

    def UpdateImage(self, delay, event=None):

        self.pil_image, self.image, self.cv_image = self.get_image()
        self.media.configure(image=self.image) # , text="Iteration %s" % self.iteration)

        # reschedule to run again in 1 second
        self.after(delay, self.UpdateImage, INTERVAL) # frame rate

    def get_image(self):
        '''
        return
        ------
        three image instances : PIL, ImageTK, OpenCV
        '''

        input_img = cap.read()[1]

        if self.task.get() == 'emotion':
            input_img = emo.detect_emotion(input_img)
        elif self.task.get() == 'C1000': # image classification on 1000 classes. use pretrained model on ImageNet
            if 'c1000' not in self.__dict__ or self.c1000 is None:
                self.c1000 = Classifier()
            self.c1000.predict_cv(input_img, anno = True)
        elif self.task.get() == 'flower': # image classification on 1000 classes. use pretrained model on ImageNet
            if 'flower' not in self.__dict__ or self.flower is None:
                self.flower = FlowerClassifier()
            self.flower.predict_cv(input_img, anno = True)
        elif self.task.get() == 'rop': # image classification on 1000 classes. use pretrained model on ImageNet
            if 'rop' not in self.__dict__ or self.rop is None:
                self.rop = RopClassifier()
            self.rop.predict_cv(input_img, anno = True)
        elif self.task.get() == 'blur':
            input_img = overlay_image(input_img)
        else:
            pass

        cv2image= cv2.cvtColor(input_img,cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)

        # Resize the image using resize() method
        # print(self.winfo_width() , self.winfo_height())
        resize_image = img.resize((self.winfo_width() , max(self.winfo_height() - 50, 1) ))
        imgtk = ImageTk.PhotoImage(resize_image)

        return img, imgtk, input_img

    ########### BUTTON CLICK EVENT HANDLER #############
    def capture_image(self):

        if not os.path.exists(SAVE_DIR):
            os.makedirs(SAVE_DIR)

        fn = SAVE_DIR + get_timestamp() + '.jpg'
        # cv2.imwrite(fn, self.cv_image)
        self.pil_image.save( fn )
        # messagebox.showinfo("Message","Hey There! I hope you are doing well.")
        
        toast = ToastNotification(
            title="图片保存成果",
            message="保存路径为" + fn,
            duration=1000,
        )
        toast.show_toast()

    def upload_to_cloud(self):

        toast = ToastNotification(
            title="同步至云端",
            message="开发中, 功能尚未开放",
            duration=2000,
        )
        toast.show_toast()

    def open_save_folder(self):

        # import subprocess
        # subprocess.Popen("./" + SAVE_DIR + "/")
        # webbrowser.open(("./" + SAVE_DIR + "/"))    

        fapp= ttk.Toplevel(app)
        fapp.geometry(DEFAULT_WINSIZE)
        fapp.attributes('-fullscreen', ENABLE_FULLSCREEN)
        fapp.title("拍摄文件一览")
        FileSearchFrame(fapp, SAVE_DIR, fix_path=True, init=True)

    def device_info(self):

        dapp= ttk.Toplevel(app)
        dapp.geometry(DEFAULT_WINSIZE)
        dapp.attributes('-fullscreen', ENABLE_FULLSCREEN)
        dapp.title("设备信息")
        DeviceInfoFrame(dapp)

    def sde(self):
     
        # Toplevel object which will
        # be treated as a new windowcls
        newWindow = ttk.Toplevel(app)
    
        # sets the title of the
        # Toplevel widget
        newWindow.title("Data Entry")
    
        # sets the geometry of toplevel
        newWindow.geometry(DEFAULT_WINSIZE)
    
        # A Label widget to show in toplevel
        ttk.Label(newWindow,
            text ="This is a new window").pack()

    def change_style(self):
        style = ttk.Style()
        theme = choice(style.theme_names())
        style.theme_use(theme)   

    def launch_tfjsa(self):        
        os.system('python -m tfjsa.gui')

def key_handler(event):
   app.destroy()
   # sys.exit()

if __name__ == '__main__':

    app = ttk.Window("oCam", "yeti")

    app.geometry(DEFAULT_WINSIZE)
    app.attributes('-fullscreen', ENABLE_FULLSCREEN)

    if ENABLE_FULLSCREEN and sys.platform == 'win32':
        # zoomed is only valid on windows and OSX. It's not supported on X11-based systems.
        app.state('zoomed')

    mp = MainApp(app)
    
    # use either q or esc to close window
    app.bind('<q>', key_handler)
    app.bind('<Escape>', lambda event: sys.exit())

    app.mainloop()