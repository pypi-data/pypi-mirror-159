import cv2
import os

if __name__ == '__main__':

    model_means = [78.4263377603, 87.7689143744, 114.895847746]
    age_labels = ["(0-2)","(4-6)","(8-12)","(15-20)","(25-32)","(38-43)","(48-53)","(60-100)"]
    gender_labels = ["Male","Female"]
    padding = 20

    '''
    cv2.IMREAD_COLOR: It specifies to load a color image. Any transparency of image will be neglected. It is the default flag. Alternatively, we can pass integer value 1 for this flag.
    cv2.IMREAD_GRAYSCALE: It specifies to load an image in grayscale mode. Alternatively, we can pass integer value 0 for this flag.
    cv2.IMREAD_UNCHANGED: It specifies to load an image as such including alpha channel. Alternatively, we can pass integer value -1 for this flag.
    '''
    frame = cv2.imread(os.path.dirname(__file__) + '/sample1.jpg', cv2.IMREAD_COLOR)

    ageNet = cv2.dnn.readNetFromCaffe(os.path.dirname(__file__) +  "/age_deploy.prototxt",
    os.path.dirname(__file__) + "/age_net.caffemodel");
    genderNet = cv2.dnn.readNetFromCaffe(os.path.dirname(__file__) + "/gender_deploy.prototxt",
    os.path.dirname(__file__) + "/gender_net.caffemodel");
    faceNet = cv2.dnn.readNetFromCaffe(os.path.dirname(__file__) + "/opencv_face_detector.pbtxt",
    os.path.dirname(__file__) + "/opencv_face_detector_uint8.pb");

    blob = cv2.dnn.blobFromImage(frame, 1, (300,300), (104, 117, 123), True, False)
        
    # TODO: research later.
    # faceNet.setInput(blob)
    # net.cpp:79: error: (-215:Assertion failed) !empty() in function 'cv::dnn::dnn4_v20220524::Net::forward'
    # detections = faceNet.forward()
    
    # print(detections)