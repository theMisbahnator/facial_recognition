from face_rec_local import encode_image, saveEncoding
import AwsHandler as aws
import query as query
import numpy as np
import base64
import json


def addSongInfo(name, userID, yt_url) :
    mp3_fn = "{}_{}_song.mp3".format(name, userID)
    song_title = aws.downloadVideo(yt_url, mp3_fn)
    aws.uploadFile(mp3_fn, mp3_fn)
    return mp3_fn, song_title


def addFaceInfo(name, userID, cur_img_fn) :
    img_fn = "{}_{}_face.jpg".format(name, userID)
    img_enc_fn = "{}_{}_face_enc.npy".format(name, userID)
    saveEncoding(encode_image(cur_img_fn), img_enc_fn)
    aws.uploadFile(img_enc_fn, img_enc_fn)
    aws.uploadFile(cur_img_fn, img_fn)
    return img_fn, img_enc_fn


def addUser(name, yt_url, cur_img_fn) :
    # insert name into table, with time stamp of upload/modify date
    userID = query.sqlAddName(name)
    # song stuff
    mp3_fn, song_title = addSongInfo(name, userID, yt_url)
    # face stuff
    img_fn, img_enc_fn = addFaceInfo(name, userID, cur_img_fn)
    # add users to db 
    return query.sqlAddUser(userID, name, yt_url, mp3_fn, song_title, img_fn, img_enc_fn)


def modifyUserSong(name, userID, yt_url) :
    old_mp3_fn = query.sqlGetMP3Name(userID)
    aws.deleteFile(old_mp3_fn)
    mp3_fn, song_title = addSongInfo(name, userID, yt_url)
    query.sqlModifySong(userID, mp3_fn, song_title, yt_url)


def modifyUserPhoto(name, userID, new_img_fn) :
    old_img = query.sqlGetImgName(userID)
    old_img_enc = query.sqlGetImgEncName(userID)
    aws.deleteFile(old_img)
    aws.deleteFile(old_img_enc)
    img_fn, img_enc_fn = addFaceInfo(name, userID, new_img_fn)
    query.sqlModifyFaceImg(userID, img_fn, img_enc_fn)


def deleteUserData(userID) :
    old_img = query.sqlGetImgName(userID)
    old_img_enc = query.sqlGetImgEncName(userID)
    old_mp3_fn = query.sqlGetMP3Name(userID)
    aws.deleteFile(old_img)
    aws.deleteFile(old_img_enc)
    aws.deleteFile(old_mp3_fn)
    return query.sqlDeleteRecord(userID)

def getAllImgEncs() :
    list_of_encs = query.sqlGetImgEncs()
    keys = ["name", "file_name"]
    dict_of_users = []
    for enc in list_of_encs :
        dict_of_users.append(query.convertToDict(enc, keys))
    
    for user in dict_of_users :
        fileName = user["file_name"]
        aws.getFileDownload(fileName)
        encoding = np.load(fileName)
        aws.removeFile(fileName)
        user["content"] = encoding.tolist()

    return json.dumps(dict_of_users)
    

def createImg(b64_string) :
    b64_string = b64_string.encode('ascii')
    with open('encode.bin', "wb") as file:
        file.write(b64_string)
    file = open('encode.bin', 'rb')
    byte = file.read()
    file.close()
    decodeit = open('img.jpg', 'wb')
    decodeit.write(base64.b64decode((byte)))
    decodeit.close()
    aws.removeFile('encode.bin')
    return 'img.jpg'

def loadImg(userID) :
    fileName = query.sqlGetImgName(userID)
    aws.getFileDownload(fileName)
    with open('./{}'.format(fileName), "rb") as img_file:
        b64_encoding = base64.b64encode(img_file.read())
    b64_string = b64_encoding.decode('utf-8')
    aws.removeFile(fileName)
    return b64_string
    


# addUser("nabil", "https://www.youtube.com/watch?v=9-tfkd9vnnA&ab_channel=ek1", "nabil.jpg")
# addUser("sarim", "https://www.youtube.com/watch?v=V7UgPHjN9qE&ab_channel=DrakeVEVO", "sarim.jpg")
# addUser("taha", "https://www.youtube.com/watch?v=OrYjTUbyLZ4&ab_channel=ChiefKeef-Topic", "taha.jpg")
# modifyUserSong("misbah", "11", "https://www.youtube.com/watch?v=9-tfkd9vnnA&list=RD9-tfkd9vnnA&start_radio=1&ab_channel=ek1")
# modifyUserPhoto("misbah", 10, "sarim.jpg")
# deleteUserData(10)
