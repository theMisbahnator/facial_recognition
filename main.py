import cv2
import face_recognition as fr
import numpy as np
import os
import glob

# i installed these libraries
# pip install cmake face_recognition numpy opencv-python

webcam = cv2.VideoCapture(0)


def encode_image(path):
    img = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
    img_encoding = fr.face_encodings(img)[0]
    return img_encoding


# result = face_recognition.compare_faces([encode_image("faces/nabil.jpg")], encode_image("Misbah.jpg"))
# print("Result: ", result)

curPath = os.path.join(os.getcwd(), "faces/")
registered_photos = glob.glob(curPath + '*.jpg')
num_of_photos = len(registered_photos)
names = []
registered_encodings = []

# saving and encoding known names
for photos in registered_photos:
    names.append(str(photos).replace(curPath, "").replace('.jpg', ""))
    registered_encodings.append(encode_image(photos))

# # code from Behic Guven
# for i in range(num_of_photos):
#     globals()['image_{}'.format(i)] = face_recognition.load_image_file(registered_photos[i])
#     globals()['image_encoding_{}'.format(i)] = face_recognition.face_encodings(globals()['image_{}'.format(i)])[0]
#     faces_encodings.append(globals()['image_encoding_{}'.format(i)])

while True:
    # Display current frame
    ret, frame = webcam.read()
    cv2.imshow("frame:", frame)

    # encode all faces on the frame (could be more than one face detected)
    face_encodings = fr.face_encodings(frame, fr.face_locations(frame))

    # press q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()

# encode the image in order to compare it to other images
