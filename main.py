import cv2
import face_recognition as face_rec
import numpy as np
import os
import glob
import time


# takes an image and returns the image encoding
# MATH Explained:
def encode_image(path):
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


def encode_face_from_frames(face_locations, face_encodings, this_frame):
    found_names = []
    for cur_face_location, cur_face_encoding in zip(face_locations, face_encodings):
        face_distance = face_rec.face_distance(registered_encodings, cur_face_encoding)
        matches = face_rec.compare_faces(registered_encodings, cur_face_encoding, tolerance=0.5)
        identified = "Unknown"
        best_match_index = np.argmin(face_distance)
        if matches[best_match_index]:
            identified = names[best_match_index]
            found_names.append(identified)
        this_frame = draw_rectangle(cur_face_location, this_frame, identified, 2)
    return found_names


curPath = os.path.join(os.getcwd(), "faces/")
registered_photos = glob.glob(curPath + '*.jpg')
num_of_photos = len(registered_photos)
names = []
registered_encodings = []

prevTime = 0
curTime = 1

# saving and encoding known names
for photos in registered_photos:
    names.append(str(photos).replace(curPath, "").replace('.jpg', ""))
    registered_encodings.append(encode_image(photos))

webcam = cv2.VideoCapture(0)
while True:
    # Display current frame
    ret, frame = webcam.read()
    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=.5, fy=.5)
    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]
    # locate and encode all faces on the frame (could be more than one face detected)
    face_locations = face_rec.face_locations(rgb_small_frame)
    face_encodings = face_rec.face_encodings(rgb_small_frame, face_locations)

    match = encode_face_from_frames(face_locations, face_encodings, frame)
    print("found a match: ", match)
    cv2.imshow('Webcam_face_recognition', frame)

    # press q to exit, later integrate this functionality with an app
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
