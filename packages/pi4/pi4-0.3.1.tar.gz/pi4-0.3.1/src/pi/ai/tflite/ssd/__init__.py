'''
TODO: the inference is slow. research later.
'''
import numpy as np
import time
import cv2
import tensorflow as tf
# from tensorflow.keras.preprocessing import image
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from tensorflow.keras.applications import mobilenet_v3, efficientnet
# For MobileNetV3, by default input preprocessing is included as a part of the model (as a Rescaling layer), and thus tf.keras.applications.mobilenet_v3.preprocess_input is actually a pass-through function. In this use case, MobileNetV3 models expect their inputs to be float tensors of pixels with values in the [0-255] range.

import os
import sys

if __package__:
    from ...emo import text_on_detected_boxes
else:
    EMO_DIR = os.path.dirname (os.path.dirname (os.path.dirname(__file__)) )
    if EMO_DIR not in sys.path:
        sys.path.append(EMO_DIR)
    # print(EMO_DIR)
    from emo import text_on_detected_boxes

class Detector:

    # The init method or constructor
    def __init__(self, model_path = None, labels = None):

        '''
        model : model's absolute path
        labels : a list of class names

        By default, will use the pretrained mobilenet v3 model on imagenet.
        '''
        self.task = 'unknown'

        if model_path is None:

            MODEL_FILE = '/detect.tflite' # "/lite-model_efficientdet_lite4_detection_metadata_2.tflite"
            model_path = os.path.dirname(__file__) + MODEL_FILE
            self.task = 'COCO'

        # Load TFLite model and allocate tensors.
        self.interpreter = tf.lite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()

        # Get input and output tensors.
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()
        
        if labels is None:

            LABEL_FILE = '/COCO_labels.txt'
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
        h, w, c = img.shape
        pil_img = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
        detection_locations, detection_classes, detection_scores, num_detections = self.predict_pil(pil_img)

        # print(detection_locations, detection_classes, detection_scores, num_detections)

        if anno:

            numDetectionsOutput = int(np.minimum(num_detections[0],3))

            for i in range(numDetectionsOutput):

                # Create a Rectangle patch
                inputSize = 300
                left = detection_locations[0][i][1] * w
                top = detection_locations[0][i][0] * h
                right = detection_locations[0][i][3] * w
                bottom = detection_locations[0][i][2] * h

                cv2.rectangle(img, (round(left), round(top)), (round(right), round(bottom)), (0, 255, 0), 2)

                class_name = self.labels[int(detection_classes[0][i])]
                text_anno = class_name + " "+ str(round(detection_scores[0][i], 3))
                # rect = patches.Rectangle((left, bottom), right-left, top-bottom, linewidth=1, edgecolor='r', facecolor='none')

                text_on_detected_boxes(text_anno, round(left), round(top), img)

        return img

    def predict_pil(self, img): 
        '''
        img : a PIL image, RGB ranges 0-255. We will later rescale to 0-1
        '''
        input_shape = self.input_details[0]['shape']
        resized = img.resize((input_shape[1], input_shape[2])) # np.array(np.random.random_sample(input_shape), dtype=np.float32)

        # if COCO:   
        x = np.array(resized)
        x = np.expand_dims(x, axis=0)
        # x = efficientnet.preprocess_input(x)
        x = np.array(x, dtype=np.uint8)

        self.interpreter.set_tensor(self.input_details[0]['index'], x)
        self.interpreter.invoke()

        detection_locations = self.interpreter.get_tensor(self.output_details[0]['index'])
        detection_classes = self.interpreter.get_tensor(self.output_details[1]['index'])
        detection_scores = self.interpreter.get_tensor(self.output_details[2]['index'])
        num_detections = self.interpreter.get_tensor(self.output_details[3]['index'])

        return detection_locations, detection_classes, detection_scores, num_detections

if __name__ == '__main__':

    CAMERA_ID = 0
    cap = cv2.VideoCapture(CAMERA_ID)
    dt = Detector()

    # while True:

    #    cv2image= cap.read()[1]
    cv2image= cv2.imread(os.path.dirname(__file__) + '/tabby.jpeg')
    img = dt.predict_cv(cv2image, anno = True)
    cv2.imshow('All', img)
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

