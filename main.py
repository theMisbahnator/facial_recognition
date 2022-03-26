import cv2
import face_recognition as face_rec
import numpy as np
import os
import glob

# takes an image and returns the image encoding
# MATH Explained:
def encode_image(path):
    img = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
    img_encoding = face_rec.face_encodings(img)[0]
    return img_encoding


def draw_rectangle(face_location, this_frame, name):
    y1, x1, y2, x2 = face_location[0] * 10, face_location[1] * 10, face_location[2] * 10, face_location[3] * 10
    cv2.rectangle(this_frame, (x2, y1), (x1, y2), (0, 0, 255), 2)
    cv2.rectangle(this_frame, (x2, y2 - 35), (x1, y2), (0, 0, 255), cv2.FILLED)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(this_frame, name, (x2 + 6, y2 - 6), font, 1.0, (255, 255, 255), 1)
    return this_frame


curPath = os.path.join(os.getcwd(), "faces/")
registered_photos = glob.glob(curPath + '*.jpg')
num_of_photos = len(registered_photos)
names = []
registered_encodings = []

# saving and encoding known names
for photos in registered_photos:
    names.append(str(photos).replace(curPath, "").replace('.jpg', ""))
    registered_encodings.append(encode_image(photos))

doit = True

webcam = cv2.VideoCapture(0)
while True:
    # Display current frame
    ret, frame = webcam.read()
    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.1, fy=0.1)
    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]
    # locate and encode all faces on the frame (could be more than one face detected)
    face_locations = face_rec.face_locations(rgb_small_frame)
    face_encodings = face_rec.face_encodings(rgb_small_frame, face_locations)

    # take current encoding and face location on frame, compare it to all known encodings
    for cur_face_location, cur_face_encoding in zip(face_locations, face_encodings):
        face_distance = face_rec.face_distance(registered_encodings, cur_face_encoding)
        matches = face_rec.compare_faces(registered_encodings, cur_face_encoding)
        identified = "Unknown"
        best_match_index = np.argmin(face_distance)
        if matches[best_match_index]:
            identified = names[best_match_index]
        frame = draw_rectangle(cur_face_location, frame, identified)
    cv2.imshow('Webcam_face_recognition', frame)

    # press q to exit, later integrate this functionality with an app
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
