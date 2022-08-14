import cv2
import face_recognition as face_rec
import numpy as np

def saveEncoding(encoding, fileName) :
    np.save(fileName, encoding)

def getEncoding(fileName) :
    return np.load(fileName)

# takes an image and returns the image encoding
# MATH Explained:
def encode_image(path):
    print(path)
    img = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
    img_encoding = face_rec.face_encodings(img)[0]
    return img_encoding


def draw_rectangle(face_location, this_frame, name, factor):
    y1, x1, y2, x2 = face_location[0] * factor, face_location[1] * factor, face_location[2] * factor, face_location[3] * factor
    cv2.rectangle(this_frame, (x2, y1), (x1, y2), (0, 0, 255), 2)
    cv2.rectangle(this_frame, (x2, y2 - 35), (x1, y2), (0, 0, 255), cv2.FILLED)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(this_frame, name, (x2 + 6, y2 - 6), font, 1.0, (255, 255, 255), 1)
    return this_frame

