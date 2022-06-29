
import cv2
import face_recognition as face_rec
import face_rec_local as frl
import numpy as np
import query

import time
import ThemeSong

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
        # this_frame = draw_rectangle(cur_face_location, this_frame, identified, 2)
    return found_names



names = []
registered_encodings = []
list_encs = query.sqlGetImgEncs()
for tup_enc in list_encs :
    fileName = tup_enc[0]
    ThemeSong.getEncFile(fileName)
    encoding = np.load(fileName)
    ThemeSong.removeFile(fileName)
    split = fileName.rsplit("_")
    names.append(split[0] + "_" + split[1])
    registered_encodings.append(encoding)


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
    if len(match) > 0 and match[0] == curName:
        curStreak = curStreak + 1
        if curStreak == 2:
            print("playing audio")
            ThemeSong.playMusic(query.sqlGetMP3Name(match[0].rsplit("_")[1]), 20)
            curStreak = 0
            curName = ""
    else:
        curStreak = 0
        curName = "" if len(match) == 0 else match[0]
    cv2.imshow('Webcam_face_recognition', frame)

    # press q to exit, later integrate this functionality with an app
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
