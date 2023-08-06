import os
import sys
import time
from datetime import datetime
from pathlib import Path
import cv2
from PIL import Image, ImageTk, ImageDraw,ImageFont
from threading import *

import ttkbootstrap as ttk
from tkinter.filedialog import askdirectory
from ttkbootstrap.dialogs import Messagebox
from ttkbootstrap.constants import *
from tkinter.scrolledtext import ScrolledText
from ttkbootstrap.toast import ToastNotification

'''
About binding keys to functions, refer to: 
https://tkinterexamples.com/events/keyboard/
'''

LCD_DRIVER_I = False # we provide two vers of lcd driver

if __package__:
    from . import led, acc, servo, joystick
    from . import passive_buzzer as pbz
    from . import PCF8591 as adc
    from . import ds18b20 as temperature
    from .setting_frame import SettingFrame
    from . import LCD1602 as lcd
    from .liquidcrystal_i2c import LiquidCrystal_I2C
    from ..gui import CollapsableFrame
else:
    import led, acc, servo, joystick
    import passive_buzzer as pbz
    import PCF8591 as adc
    import ds18b20 as temperature
    from setting_frame import SettingFrame
    import LCD1602 as lcd
    from liquidcrystal_i2c import LiquidCrystal_I2C

    GUI_DIR = os.path.dirname (os.path.dirname(__file__))
    if GUI_DIR not in sys.path:
        sys.path.append(GUI_DIR)
    print(GUI_DIR)

    from gui import CollapsableFrame

CAMERA_ID = 0
cap = cv2.VideoCapture(CAMERA_ID)
INTERVAL = 100 # ms
LIVEVIEW_SIZE = (240,180)
SAVE_DIR = 'ocam_captures/'

DEFAULT_WINSIZE = '500x400'
ENABLE_FULLSCREEN = False
TREEVIEW_ROW_HEIGHT = 21

TEST_LED = '1'
TEST_PASSIVE_BUZZER = '3'
TEST_LCD = '11'
TEST_SERVO = '4'
TEST_RA = '8'
TEST_JOYSTICK = '2'
TEST_ADC = '5'
TEST_LASER = '6' # Laser pin is connected to LED Blue Pin
TEST_W1 = '7'
TEST_ACC = '10'

PATH = Path(__file__).parent.parent / 'gui/gallery/assets'

class MainGui(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack(fill=BOTH, expand=YES)        

        led.RUNNING = False
        # led.setup() # called inside acc.setup()
        temperature.setup()
        pbz.RUNNING = False
        # pbz.setup() # Share with RGB LED Bpin. called inside acc.setup()
        # servo.setup()  # called inside acc.setup()
        joystick.RUNNING = False
        adc.RUNNING = False
        acc.RUNNING = False
        acc.setup()
        acc.print_used_pins()        

        image_files = {
            'properties-dark': 'icons8_settings_24px.png',
            'properties-light': 'icons8_settings_24px_2.png',
            'add-to-backup-light': 'icons8_add_book_24px.png',
            'stop-backup-dark': 'icons8_cancel_24px.png',
            'stop-backup-light': 'icons8_cancel_24px_1.png',
            'play': 'icons8_play_24px_1.png',
            'refresh': 'icons8_refresh_24px_1.png',
            'stop-dark': 'icons8_stop_24px.png',
            'stop-light': 'icons8_stop_24px_1.png',
            'opened-folder': 'icons8_opened_folder_24px.png',
            'logo': 'backup.png',
            # 'splash': 'splash.png', # support png, but dont support jpg
        }


        self.photoimages = []
        for key, val in image_files.items():
            _path = PATH / val
            self.photoimages.append(ttk.PhotoImage(name=key, file=_path))

        if False:
            # buttonbar
            buttonbar = ttk.Frame(self, style='primary.TFrame')
            buttonbar.pack(fill=X, pady=1, side=TOP)

            ## new backup
            _func = lambda: Messagebox.ok(message='Adding new backup')
            btn = ttk.Button(
                master=buttonbar, text='New backup set',
                image='add-to-backup-light', 
                compound=LEFT, 
                command=_func
            )
            btn.pack(side=LEFT, ipadx=5, ipady=5, padx=(1, 0), pady=1)

            ## backup
            _func = lambda: Messagebox.ok(message='Backing up...')
            btn = ttk.Button(
                master=buttonbar, 
                text='Backup', 
                image='play', 
                compound=LEFT, 
                command=_func
            )
            btn.pack(side=LEFT, ipadx=5, ipady=5, padx=0, pady=1)

            ## refresh
            _func = lambda: Messagebox.ok(message='Refreshing...')
            btn = ttk.Button(
                master=buttonbar, 
                text='Refresh', 
                image='refresh',
                compound=LEFT, 
                command=_func
            )
            btn.pack(side=LEFT, ipadx=5, ipady=5, padx=0, pady=1)

            ## stop
            btn = ttk.Button(
                master=buttonbar, 
                text='Stop', 
                image='stop-light',
                compound=LEFT, 
                command=self.stop
            )
            btn.pack(side=LEFT, ipadx=5, ipady=5, padx=0, pady=1)

            ## settings
            _func = lambda: Messagebox.ok(message='Changing settings')
            btn = ttk.Button(
                master=buttonbar, 
                text='Settings', 
                image='properties-light',
                compound=LEFT, 
                command=_func
            )
            btn.pack(side=LEFT, ipadx=5, ipady=5, padx=0, pady=1)

        # left panel
        left_panel = ttk.Frame(self, style='bg.TFrame')
        left_panel.pack(side=LEFT, fill=Y)

        bus_cf = CollapsableFrame(left_panel)
        bus_cf.pack(fill=X, pady=1)

        ## container
        bus_frm = ttk.Frame(bus_cf, padding=5)
        bus_frm.columnconfigure(1, weight=1)
        bus_cf.add(
            child=bus_frm, 
            title='Camera', 
            bootstyle=SECONDARY)

        ## Camera liveview
        self.media = ttk.Label(bus_frm, image='logo', style='bg.TLabel') # , image=self.demo_media)
        self.media.bind('<Double-1>', self.change_liveview_size)
        self.media.grid(row=0, column=0, columnspan=3, sticky=N+S+E+W) # .pack(fill=BOTH, expand=YES)
        self.liveview_size=LIVEVIEW_SIZE
        self.UpdateImage(INTERVAL)

        ## camera pan tilt control
        _func = lambda: servo.pan_tilt_left()
        add_btn = ttk.Button(
            master=bus_frm, 
            text='LEFT', 
            compound=LEFT,
            command=_func, 
            bootstyle=LINK
        )
        add_btn.grid(row=5, column=0, rowspan=1, sticky=W)
        self.master.bind('<Left>',lambda x: servo.pan_tilt_left())

        _func = lambda: servo.pan_tilt_up()
        add_btn = ttk.Button(
            master=bus_frm, 
            text='UP', 
            compound=TOP,
            command=_func, 
            bootstyle=LINK
        )
        add_btn.grid(row=4, column=1, rowspan=1, sticky=N)
        self.master.bind('<Up>',lambda x: servo.pan_tilt_up())

        _func = lambda: servo.pan_tilt_down()
        add_btn = ttk.Button(
            master=bus_frm, 
            text='DOWN', 
            compound=BOTTOM,
            command=_func, 
            bootstyle=LINK
        )
        add_btn.grid(row=6, column=1, rowspan=1, sticky=S)
        self.master.bind('<Down>',lambda x: servo.pan_tilt_down())

        _func = lambda: servo.pan_tilt_right()
        add_btn = ttk.Button(
            master=bus_frm, 
            text='RIGHT', 
            compound=LEFT,
            command=_func, 
            bootstyle=LINK
        )
        add_btn.grid(row=5, column=2, rowspan=1, sticky=E)
        self.master.bind('<Right>',lambda x: servo.pan_tilt_right())
        
        
        _func = lambda: servo.reset_tilt()
        add_btn = ttk.Button(
            master=bus_frm, 
            text='RESET', 
            compound=LEFT,
            command=_func, 
            bootstyle=LINK
        )
        add_btn.grid(row=5, column=1, rowspan=1, sticky=E)
        self.master.bind('<r>',lambda x: servo.reset_tilt())

        self.master.bind('<Return>', lambda x: self.capture_image())

        ################## VEHICLE ######################

        v_cf = CollapsableFrame(left_panel)
        v_cf.pack(fill=X, pady=1)

        ## container
        v_frm = ttk.Frame(v_cf, padding=5)
        v_frm.columnconfigure(1, weight=1)
        v_cf.add(
            child=v_frm, 
            title='Vehicle', 
            bootstyle=SECONDARY)

        
        ## vehicle control
        _func = lambda: acc.turn_left()
        add_btn = ttk.Button(
            master=v_frm, 
            text='LEFT', 
            compound=LEFT,
            command=_func, 
            bootstyle=LINK
        )
        add_btn.grid(row=5, column=0, rowspan=1, sticky=W)
        self.master.bind('<a>',lambda x: acc.turn_left() )

        _func = lambda: acc.move_forward()
        add_btn = ttk.Button(
            master=v_frm, 
            text='FORWARD', 
            compound=TOP,
            command=_func, 
            bootstyle=LINK
        )
        add_btn.grid(row=4, column=1, rowspan=1, sticky=N)
        self.master.bind('<w>', lambda x: acc.move_forward() )

        _func = lambda: acc.move_backward()
        add_btn = ttk.Button(
            master=v_frm, 
            text='BACKWARD', 
            compound=BOTTOM,
            command=_func, 
            bootstyle=LINK
        )
        add_btn.grid(row=6, column=1, rowspan=1, sticky=S)
        self.master.bind('<x>',lambda x: acc.move_backward() )

        _func = lambda: acc.turn_right()
        add_btn = ttk.Button(
            master=v_frm, 
            text='RIGHT', 
            compound=LEFT,
            command=_func, 
            bootstyle=LINK
        )
        add_btn.grid(row=5, column=2, rowspan=1, sticky=E)
        self.master.bind('<d>',lambda x: acc.turn_right())

        _func = lambda: acc.stop()
        add_btn = ttk.Button(
            master=v_frm, 
            text='STOP', 
            compound=LEFT,
            command=_func, 
            bootstyle=LINK
        )
        add_btn.grid(row=5, column=1, rowspan=1, sticky=E)
        self.master.bind('<s>',lambda x: acc.stop())

        ## section separator
        sep = ttk.Separator(v_frm, bootstyle=SECONDARY)
        sep.grid(row=9, column=0, columnspan=3, pady=10, sticky=EW)


        h_container = ttk.Frame(left_panel)
        h_container.pack(fill=X, expand=YES)
        ## stop button
        btn = ttk.Button(
            master=h_container, 
            text='Stop', 
            image='stop-backup-dark', 
            compound=LEFT, 
            command=self.stop, 
            bootstyle=LINK
        )
        btn.pack(side=LEFT, fill=X, expand=YES) #.grid(row=0, column=0, columnspan=1, sticky=W)
        self.master.bind('<space>',lambda x: self.stop())

        btn = ttk.Button(
            master=h_container, 
            text='Config', 
            image='properties-dark', 
            compound=LEFT,
            command=self.open_settings, 
            bootstyle=LINK
        )
        btn.pack(side=LEFT, fill=X, expand=YES) #.grid(row=0, column=1, columnspan=1, sticky=W)


        ################## RA ######################

        v_cf = CollapsableFrame(left_panel)
        v_cf.pack(fill=X, pady=1)

        ## container
        v_frm = ttk.Frame(v_cf, padding=5)
        v_frm.columnconfigure(1, weight=1)
        v_cf.add(
            child=v_frm, 
            title='robotic arm', 
            bootstyle=SECONDARY)

        _func = lambda: servo.ra_left()
        add_btn = ttk.Button(
            master=v_frm, 
            text='LEFT', 
            compound=LEFT,
            command=_func, 
            bootstyle=LINK
        )
        add_btn.grid(row=5, column=0, rowspan=2, sticky=W)
        self.master.bind('<j>',lambda x: servo.ra_left() )

        _func = lambda: servo.ra_f()
        add_btn = ttk.Button(
            master=v_frm, 
            text='FORWARD', 
            compound=TOP,
            command=_func, 
            bootstyle=LINK
        )
        add_btn.grid(row=5, column=1, rowspan=1, sticky=N)
        self.master.bind('<i>', lambda x: servo.ra_f() )

        _func = lambda: servo.ra_b()
        add_btn = ttk.Button(
            master=v_frm, 
            text='BACKWARD', 
            compound=BOTTOM,
            command=_func, 
            bootstyle=LINK
        )
        add_btn.grid(row=6, column=1, rowspan=1, sticky=S)
        self.master.bind('<comma>',lambda x: servo.ra_b() )

        _func = lambda: servo.ra_right()
        add_btn = ttk.Button(
            master=v_frm, 
            text='RIGHT', 
            compound=LEFT,
            command=_func, 
            bootstyle=LINK
        )
        add_btn.grid(row=5, column=2, rowspan=2, sticky=E)
        self.master.bind('<l>',lambda x: servo.ra_right())

        ## section separator
        sep = ttk.Separator(v_frm, bootstyle=SECONDARY)
        sep.grid(row=7, column=0, columnspan=3, pady=10, sticky=EW)


        _func = lambda: servo.ra_up()
        add_btn = ttk.Button(
            master=v_frm, 
            text='UP', 
            compound=LEFT,
            command=_func, 
            bootstyle=LINK
        )
        add_btn.grid(row=8, column=0, rowspan=1, sticky=E)
        self.master.bind('<u>',lambda x: servo.ra_up())

        _func = lambda: servo.ra_down()
        add_btn = ttk.Button(
            master=v_frm, 
            text='DOWN', 
            compound=LEFT,
            command=_func, 
            bootstyle=LINK
        )
        add_btn.grid(row=8, column=1, rowspan=1, sticky=E)
        self.master.bind('<m>',lambda x: servo.ra_down())

        _func = lambda: servo.ra_clamp()
        add_btn = ttk.Button(
            master=v_frm, 
            text='CLAMP', 
            compound=LEFT,
            command=_func, 
            bootstyle=LINK
        )
        add_btn.grid(row=8, column=2, rowspan=1, sticky=E)
        self.master.bind('<period>',lambda x: servo.ra_clamp())
        self.master.bind('<o>',lambda x: servo.ra_clamp())

        ############## STATUS Panel ################
        # status (collapsible)
        status_cf = CollapsableFrame(left_panel)
        status_cf.pack(fill=BOTH, pady=1)

        ## container
        status_frm = ttk.Frame(status_cf, padding=10)
        status_frm.columnconfigure(1, weight=1)
        status_cf.add(
            child=status_frm, 
            title='Status', 
            bootstyle=SECONDARY
        )

        import socket
        h_name = socket.gethostname()
        IP_addres = socket.gethostbyname(h_name)
        dev_ip = "Host Name:" + h_name 

        lbl = ttk.Label(status_frm, text='Host:')
        lbl.grid(row=0, column=0, sticky=W, pady=2)
        lbl = ttk.Label(status_frm, text = h_name)
        lbl.grid(row=0, column=1, sticky=EW, padx=5, pady=2)

        lbl = ttk.Label(status_frm, text='IP:')
        lbl.grid(row=1, column=0, sticky=W, pady=2)
        lbl = ttk.Label(status_frm, text = IP_addres)
        lbl.grid(row=1, column=1, sticky=EW, padx=5, pady=2)        

        import psutil
        lbl = ttk.Label(status_frm, text='CPU:')
        lbl.grid(row=2, column=0, sticky=W, pady=2)
        lbl = ttk.Label(status_frm, textvariable='cpu_info')
        lbl.grid(row=2, column=1, sticky=EW, padx=5, pady=2)
        self.setvar('cpu_info', str(psutil.cpu_freq().max) + 'MHz x ' + str(psutil.cpu_count(logical=False)) )


        lbl = ttk.Label(status_frm, text='Speed:')
        lbl.grid(row=3, column=0, sticky=W, pady=2)
        scale = ttk.Scale(
            master=status_frm,
            orient=HORIZONTAL,
            from_=30,
            to=60,
            value=acc.SPEED,
            command=self.set_speed,
            bootstyle=INFO # SUCCESS
        )
        scale.grid(row=3, column=1, columnspan=2, sticky=EW, padx=5, pady=2)


        ttk.Label(status_frm, text='FPS:').grid(row=4, column=0, sticky=W, pady=2)
        scale2 = ttk.Scale(
            master=status_frm,
            orient=HORIZONTAL,
            from_=200,
            to=10,
            value=INTERVAL, # default 200
            command=self.set_fps,
            bootstyle=INFO # SUCCESS
        )
        scale2.grid(row=4, column=1, columnspan=2, sticky=EW, padx=5, pady=2)


        ## section separator
        sep = ttk.Separator(status_frm, bootstyle=SECONDARY)
        sep.grid(row=5, column=0, columnspan=3, pady=10, sticky=EW)

        ## progress message
        lbl = ttk.Label(
            master=status_frm, 
            textvariable='prog-message', 
            font='Helvetica 10 bold'
        )
        lbl.grid(row=6, column=0, columnspan=3, sticky=W)
        self.setvar('prog-message', 'Running...')

        ## progress bar
        pb = ttk.Progressbar(
            master=status_frm, 
            variable='prog-value', 
            bootstyle=SUCCESS
        )
        pb.grid(row=7, column=0, columnspan=3, sticky=EW, pady=(10, 5))
        self.setvar('prog-value', 71)

        ## time started
        lbl = ttk.Label(status_frm, textvariable='prog-time-started')
        lbl.grid(row=8, column=0, columnspan=3, sticky=EW, pady=2)
        self.setvar('prog-time-started', 'Started at: 14.06.2021 19:34:56')

        ## time elapsed
        lbl = ttk.Label(status_frm, textvariable='prog-time-elapsed')
        lbl.grid(row=9, column=0, columnspan=3, sticky=EW, pady=2)
        self.setvar('prog-time-elapsed', 'Elapsed: 1 sec')

        ## time remaining
        lbl = ttk.Label(status_frm, textvariable='prog-time-left')
        lbl.grid(row=10, column=0, columnspan=3, sticky=EW, pady=2)
        self.setvar('prog-time-left', 'Left: 0 sec')

        ## section separator
        sep = ttk.Separator(status_frm, bootstyle=SECONDARY)
        sep.grid(row=11, column=0, columnspan=3, pady=10, sticky=EW)

        # current file message
        lbl = ttk.Label(status_frm, textvariable='current-file-msg')
        lbl.grid(row=12, column=0, columnspan=4, pady=2, sticky=EW)
        self.setvar('current-file-msg', 'Syncing')

        # logo
        lbl = ttk.Label(left_panel, image='logo', style='bg.TLabel')
        lbl.pack(side='bottom')

        # right panel
        right_panel = ttk.Frame(self, padding=(2, 1))
        right_panel.pack(side=RIGHT, fill=BOTH, expand=YES)
        

        ## Treeview
        tv = ttk.Treeview(right_panel, show='headings', height=10)
        tv.configure(columns=(
            'Device', 'GPIO', 'Description'
        ))
        # tv.column('Device', width=150, stretch=True)
        # 
        for col in ['Device', 'GPIO', 'Description']:
            tv.column(col, width = 100, stretch=True)
        
        for col in tv['columns']:
            tv.heading(col, text=col.title(), anchor=W)
        
        tv.pack(fill=X, pady=1)
        ttk.Style().configure('Treeview', rowheight = TREEVIEW_ROW_HEIGHT, font=('', round(TREEVIEW_ROW_HEIGHT * 0.5)))

        ## scrolling text output
        scroll_cf = CollapsableFrame(right_panel)
        scroll_cf.pack(fill=BOTH, expand=YES)


        output_container = ttk.Frame(scroll_cf, padding=1)
        _value = '''
        * Currently USED PINS:

   3V3  (1) (2)  5V    
- GPIO2 PCA9685 SDA (3) (4)  5V    
- GPIO3 PCA9685 SCL (5) (6)  GND   
- GPIO4 IR Control (7) (8)  - GPIO14 UART TX
   GND  (9) (10) - GPIO15 UART RX
* GPIO17 (11) (12) - GPIO18
- GPIO27 (13) (14) GND   
- GPIO22 (15) (16) - GPIO23
   3V3 (17) (18) - GPIO24
* GPIO10 SPI (19) (20) GND   
* GPIO9 SPI (21) (22) - GPIO25
* GPIO11 SPI (23) (24) * GPIO8 SPI0 CE0
   GND (25) (26) * GPIO7 SPI0 CE1
- GPIO0 (27) EEPROM SDA (28) - GPIO1 EEPROM SCL | CAT24C32: EEPROM 串行 32-Kb I2C
- GPIO5 (29) (30) GND   
- GPIO6 (31) (32) - GPIO12
- GPIO13 (33) (34) GND   
- GPIO19 (35) (36) - GPIO16
- GPIO26 (37) (38) - GPIO20
   GND (39) (40) - GPIO21

I2C devices:

     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:                         -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- 27 -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: 40 -- -- -- -- -- -- -- 48 -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- 57 -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: 70 -- -- -- -- -- -- --   

0x27 - LCD1602 PCF8574
0x40 - servo: PCA9685 16-channel PWM driver
0x48 - ADC: PCF8591
0x57 - SpO2 sensor
0x70 - 

To check a full list of I2C addresses, go to https://i2cdevices.org/addresses

servo channels:
0 - super-sonic
1,2 - tilt
3 - back super-sonic
4,5,6,7 - robotic arm

        '''       

        self.setvar('scroll-message', _value)
        st = ScrolledText(output_container)
        st.pack(fill=BOTH, expand=YES)
        scroll_cf.add(output_container, textvariable='scroll-message')

        # seed with sensor scripts

        ## treeview
        tv.insert('', END, TEST_LED, values = ('LED', '5,6,17', 'LED调试'))
        tv.insert('', END, TEST_LASER, values = ('Laser', '17', 'Laser'))       
        tv.insert('', END, TEST_W1, values = ('Temperature', '1-Wire', 'ds18b20'))
        tv.insert('', END, TEST_PASSIVE_BUZZER, values = ('Passive Buzzer', '17', '声音'))
        tv.insert('', END, TEST_LCD, values = ('LCD', 'I2C 0x27', 'LCD 1602+PCF8674'))
        tv.insert('', END, TEST_SERVO, values = ('Servos', 'I2C 0x40 0~7', '舵机'))
        tv.insert('', END, TEST_RA, values = ('Robotic Arm', 'I2C 0x40 4~7', '机械臂'))
        tv.insert('', END, TEST_JOYSTICK, values = ('Joystick', 'I2C 0x48 A0A1A2', 'Joystick Controller'))
        tv.insert('', END, TEST_ADC, values = ('ADC', 'I2C 0x48', 'PCF8591'))
        tv.insert('', END, TEST_ACC, values = ('Vehicle', '11', '自适应巡航ACC'))
        
        tv.bind('<Double-1>', self.on_tree_dbclicked)
        # tv.selection_set(1)
        self.tree = tv

    def on_tree_dbclicked(self, event):
        item = self.tree.selection()[0]
        # Messagebox.ok(title='clicked',message=item)
        
        if item == TEST_LED:    
            if led.RUNNING == False:
                led.RUNNING = True
                led.pwm_B.stop()
                led.pwm_B.start(0)

                self.test_led = Thread(target = led.loop)
                self.test_led.setDaemon(True)
                self.test_led.start()        

        elif item == TEST_PASSIVE_BUZZER: 
            if pbz.RUNNING == False:
                pbz.RUNNING = True
                self.test_pbz = Thread(target = pbz.loop)
                self.test_pbz.setDaemon(True)
                self.test_pbz.start()
        
        elif item == TEST_LCD: 
            
            if not LCD_DRIVER_I:

                lcd2 = LiquidCrystal_I2C()
                lcd2.noBacklight()

                cols = 16
                l1 = 'http://'.center(cols)
                l2 = 'zhangys.org.cn'.rjust(cols)

                lcd2.printline(0, l1)
                lcd2.printline(1, l2)

                return

                for i in range(cols):

                    lcd2.printline(0, l1)
                    lcd2.printline(1, l2)
                    time.sleep(1)

                    l1 = l1[-1] + l1[:-1]
                    l2 = l2[-1] + l2[:-1]
                
                time.sleep(1)
                lcd2.noBacklight()
                lcd2.clear()

            else:
                lcd.setup()
                lcd.test_lcd()
                lcd.lightoff()

        elif item == TEST_SERVO: 
            self.test_servo = Thread(target = servo.test_servo)
            self.test_servo.setDaemon(True)
            self.test_servo.start()

        elif item == TEST_RA: 
            self.test_ra = Thread(target = servo.test_ra)
            self.test_ra.setDaemon(True)
            self.test_ra.start()

        elif item == TEST_LASER: 
            self.test_laser = Thread(target = led.sos)
            self.test_laser.setDaemon(True)
            self.test_laser.start()

        elif item == TEST_W1: 
            Messagebox.ok ("Temperature : %0.3f C" % temperature.read())

        elif item == TEST_ADC: 
            if adc.RUNNING == False:
                adc.RUNNING = True
                self.test_adc = Thread(target = adc.loop()) 
                self.test_adc.setDaemon(True)
                self.test_adc.start()

        elif item == TEST_JOYSTICK: 
            if joystick.RUNNING == False:
                joystick.HANDLER = servo.pan_tilt
                joystick.RUNNING = True
                self.test_jt = Thread(target = joystick.loop()) 
                self.test_jt.setDaemon(True)
                self.test_jt.start()

        elif item == TEST_ACC: 
            if acc.RUNNING == False:
                acc.RUNNING = True
                self.change_liveview_size()
                self.test_acc = Thread(target = acc.loop)
                self.test_acc.setDaemon(True)
                self.test_acc.start()

    def open_settings(self):

        dapp= ttk.Toplevel(app)
        dapp.title("参数设置")
        SettingFrame(dapp)

    def set_speed(self,x):
        acc.SPEED = round( float(str(x)) ) # int(self.scale.get())

    # x actually means 1/FPS
    def set_fps(self,x):
        INTERVAL = round( float(str(x)) ) # int(self.scale.get())

    def stop(self):
        print('stop')

        led.RUNNING=False
        pbz.RUNNING=False
        acc.RUNNING=False
        joystick.RUNNING=False
        adc.RUNNING=False

        acc.stop()        

    def get_directory(self):
        """Open dialogue to get directory and update variable"""
        self.update_idletasks()
        d = askdirectory()
        if d:
            self.setvar('folder-path', d)

    def UpdateImage(self, delay, event=None):

        self.pil_image, self.image = self.get_image()
        self.media.configure(image=self.image) # , text="Iteration %s" % self.iteration)

        # reschedule to run again in 1 second
        self.after(delay, self.UpdateImage, INTERVAL) # frame rate

    def measure_distance(self, flags = [1,0,0,0]):
        '''
        Measure distances to avoid collision. 
        We cannot put this funciton in a side thread loop. Must use it in the main thread. e.g., 
            
            # this will not work:
            self.distance_monitor = Thread(target = self.measure_distance)
            self.distance_monitor.setDaemon(True)
            self.distance_monitor.start()

        flags : 4-bit flags for front, back, left and right detection
        '''       
        
        s = "Distances = "
        if flags[0]:
            self.distance_F = round(acc.front_detection())
            s = s + 'F' + str(self.distance_F) + ' '
            if self.distance_F < acc.SAFE_DISTANCE:
                acc.stop(0.2)
                acc.move_backward(t_time = 0.2)
                acc.stop(0.2)
        if flags[1]:
            self.distance_B = round(acc.back_detection())
            s = s + 'B' + str(self.distance_B) + ' '
            if self.distance_B < acc.SAFE_DISTANCE:
                acc.stop(0.2)
                acc.move_forward(t_time = 0.2)
                acc.stop(0.2)
        if flags[2]:
            self.distance_L = round(acc.left_detection())
            s = s + 'L' + str(self.distance_L) + ' '
        if flags[3]:
            self.distance_R = round(acc.right_detection())
            s = s + 'R' + str(self.distance_R)
        
        return s

    def get_image(self):

        cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)        

        if acc.RUNNING == False:

            s = self.measure_distance(flags=[1,0,0,0]) # update distances
            draw = ImageDraw.Draw(img)
            if sys.platform == 'win32':
                ff = os.path.dirname(__file__) + '/FreeMonoBold.ttf'
            else:
                ff = 'FreeMono.ttf'
            draw.text((10, 10), 
            s, 
            font = ImageFont.truetype(ff, 25),
            fill =(255, 255, 255))
            # draw.text((10, 10), "Distances : " + str(round(distance,1)), font=ft, fill =(255, 255, 255))

        # Resize the image using resize() method
        # print(self.winfo_width() , self.winfo_height())
        resize_image = img.resize(self.liveview_size) 
        imgtk = ImageTk.PhotoImage(resize_image)

        return img, imgtk

    def capture_image(self):

        if not os.path.exists(SAVE_DIR):
            os.makedirs(SAVE_DIR)

        fn = SAVE_DIR + datetime.now().strftime("%Y%m%d%H%M%S") + '.jpg'
        self.pil_image.save( fn )
        # messagebox.showinfo("Message","Hey There! I hope you are doing well.")
        
        toast = ToastNotification(
            title="图片保存成果",
            message="保存路径为" + fn,
            duration=1000,
        )
        toast.show_toast()

    def change_liveview_size(self, event = None):
        print(event)
        if (self.liveview_size == LIVEVIEW_SIZE):
            self.liveview_size = self.master.winfo_width() , max(self.master.winfo_height() - 50, 1)
        else:
            self.liveview_size = LIVEVIEW_SIZE # (240,180)

if __name__ == '__main__':
    
    # splash_root = ttk.Window()
    # splash_label = ttk.Label(splash_root, image='logo')
    # splash_label.pack()
    # splash_root.after(3000, lambda : splash_root.destroy())

    app = ttk.Window("Raspi Control Panel")
    app.geometry(DEFAULT_WINSIZE)
    app.attributes('-fullscreen', ENABLE_FULLSCREEN)
    MainGui(app)
    app.mainloop()
