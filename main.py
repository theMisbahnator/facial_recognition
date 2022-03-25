import cv2
import face_recognition
import numpy as np
import os
import glob

# i installed these libraries
# pip install cmake face_recognition numpy opencv-python

# webcam = cv2.VideoCapture(0)


def encode_image(path):
    img = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
    img_encoding = face_recognition.face_encodings(img)[0]
    return img_encoding


# result = face_recognition.compare_faces([encode_image("faces/nabil.jpg")], encode_image("Misbah.jpg"))
# print("Result: ", result)

curPath = os.path.join(os.getcwd(), "faces/")
registered_photos = glob.glob(curPath + '*.jpg')
num_of_photos = len(registered_photos)
names = registered_photos.copy()

print(names)
print(curPath)



# while True:
#     ret, frame = webcam.read()
#     cv2.imshow("frame:", frame)
#
#     # press q to exit
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# webcam.release()
# cv2.destroyAllWindows()

# encode the image in order to compare it to other images
