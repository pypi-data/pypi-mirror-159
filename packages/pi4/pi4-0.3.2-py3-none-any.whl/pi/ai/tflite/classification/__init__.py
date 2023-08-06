import numpy as np
import time
import cv2
import tensorflow as tf
# from tensorflow.keras.preprocessing import image
from PIL import Image
from tensorflow.keras.applications import mobilenet_v3, efficientnet
# For MobileNetV3, by default input preprocessing is included as a part of the model (as a Rescaling layer), and thus tf.keras.applications.mobilenet_v3.preprocess_input is actually a pass-through function. In this use case, MobileNetV3 models expect their inputs to be float tensors of pixels with values in the [0-255] range.

import os

class Classifier:

    # The init method or constructor
    def __init__(self, model_path = None, labels = None):

        '''
        model : model's absolute path
        labels : a list of class names

        By default, will use the pretrained mobilenet v3 model on imagenet.
        '''
        self.task = 'unknown'

        if model_path is None:

            MODEL_FILE = "/lite-model_imagenet_mobilenet_v3_large_075_224_classification_5_metadata_1.tflite"
            model_path = os.path.dirname(__file__) + MODEL_FILE
            self.task = 'C1000'

        # Load TFLite model and allocate tensors.
        self.interpreter = tf.lite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()

        # Get input and output tensors.
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

        if labels is None:

            LABEL_FILE = '/labels.txt'
            f = open(os.path.dirname(__file__) + LABEL_FILE, 'r+')
            classes = [line.replace('\n','').split(':')[-1] for line in f.readlines()]
            f.close()

            self.labels = classes

        else:

            self.labels = labels

    def predict_cv(self, img, anno = False):
        '''
        img : an opencv image object
        anno : whether output text anno on the image
        '''
        pil_img = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
        d, s = self.predict_pil(pil_img)
        if anno:
            i = 1
            for key in d:
                cv2.putText(img, key + ':' + str(round(d[key])),(5, 20*i), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
                i = i+1
        return d,s

    def predict_pil(self, img): 
        '''
        img : a PIL image, RGB ranges 0-255. We will later rescale to 0-1
        '''
        input_shape = self.input_details[0]['shape']
        resized = img.resize((input_shape[1], input_shape[2])) # np.array(np.random.random_sample(input_shape), dtype=np.float32)

        if self.task == 'C1000':
            x = np.array(np.array(resized), dtype=np.float32)
            x = np.expand_dims(x, axis=0)
            x = x/255.0            
            x = mobilenet_v3.preprocess_input(x) 
        elif self.task == 'rop' or self.task == 'flower':     
            x = np.array(resized)
            x = np.expand_dims(x, axis=0)
            x = efficientnet.preprocess_input(x)
            x = np.array(x, dtype=np.float32)
        else:
            x = np.array(resized)

        self.interpreter.set_tensor(self.input_details[0]['index'], x)
        self.interpreter.invoke()

        # The function `get_tensor()` returns a copy of the tensor data.
        # Use `tensor()` in order to get a pointer to the tensor.
        prediction = self.interpreter.get_tensor(self.output_details[0]['index'])
        # print(np.sum(prediction[0])) # not equal to 1
        top5 = np.argsort(prediction[0])[::-1][:5] # take last N item indices and reverse (ord desc)
        # print('------ top-5 predicted classes -----')
        
        s = ''
        d = {}
        for c,p in zip(np.array(self.labels)[top5], prediction[0][top5]):
            # print(c, round(p,3))  
            s = s + c + ' : ' + str( round(p,3) ) + '\n'
            d[c] = round(p,3)

        return d, s


class FlowerClassifier(Classifier):
    def __init__(self):
        MODEL_FILE = "/flower_customEfficientNetB0_model.tflite"
        model_path = os.path.dirname(__file__) + MODEL_FILE
        labels = ['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']
        super().__init__(model_path, labels)

        self.task = 'flower'

class RopClassifier(Classifier):
    def __init__(self):
        MODEL_FILE = "/fundus_C3_customEfficientNetB0_model_best2.tflite"
        model_path = os.path.dirname(__file__) + MODEL_FILE
        labels = ['Normal', 'Stage1~2', 'Stage3~4']
        super().__init__(model_path, labels)

        self.task = 'rop'

if __name__ == '__main__':

    CAMERA_ID = 0
    cap = cv2.VideoCapture(CAMERA_ID)
    cls = Classifier()

    while True:

        cv2image= cap.read()[1]
        d, s = cls.predict_cv(cv2image)
        time.sleep(1)

        # fps = cap.get(cv2.CAP_PROP_FPS)
        # cv2.putText(cv2image, 'FPS ' + str(round(fps)),(5, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, # 255, 255), 1)

        i = 1
        for key in d:
            cv2.putText(cv2image, key + ':' + str(round(d[key])),(5, 20*i), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
            i = i+1

        cv2.imshow('All', cv2image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

