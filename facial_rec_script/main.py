import cv2
import face_recognition as face_rec
import numpy as np
from SongPlayer import playMusic
import time
import requests
import json

# pip install requests pygame face-recognition opencv-python


BASE = "http://127.0.0.1:5000/"

def encode_face_from_frames(face_locations, face_encodings, this_frame):
    found_names = []
    for cur_face_location, cur_face_encoding in zip(face_locations, face_encodings):
        face_distance = face_rec.face_distance(registered_encodings, cur_face_encoding)
        matches = face_rec.compare_faces(registered_encodings, cur_face_encoding, tolerance=0.5)
        identified = "Unknown"
        best_match_index = np.argmin(face_distance)
        if matches[best_match_index]:
            identified = names[best_match_index]
            userID = userIDs[best_match_index]
            found_names.append(tuple((identified, userID)))
        # this_frame = draw_rectangle(cur_face_location, this_frame, identified, 2)
    return found_names



# init()
names = []
registered_encodings = []
list_encs = json.loads(requests.get(BASE + "/encodings").json())
userIDs = []
for enc in list_encs :
    names.append(enc['name'])
    userIDs.append(enc["userID"])
    registered_encodings.append(np.array(enc['content']))

prevTime = 0
curTime = 1

webcam = cv2.VideoCapture(0)
curName = ""
curStreak = 0

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
    if len(match) > 0 :
        print(match[0][0])
    if len(match) > 0 and match[0][0] == curName:
        curStreak = curStreak + 1
        if curStreak == 2:
            print("playing audio")
            # make a get request for the signed url
            yt_url = requests.get(BASE + 'songs/{}'.format(match[0][1])).json()
            playMusic(yt_url['signedurl'], 20)
            curStreak = 0
            curName = ""
    else:
        curStreak = 0
        curName = "" if len(match) == 0 else match[0][0]
    # cv2.imshow('Webcam_face_recognition', frame)

    # press q to exit, later integrate this functionality with an app
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
