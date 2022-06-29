from face_rec_local import encode_image, saveEncoding
import ThemeSong
import query


def addSongInfo(name, userID, yt_url) :
    mp3_fn = "{}_{}_song.mp3".format(name, userID)
    song_title = ThemeSong.downloadVideo(yt_url, mp3_fn)
    ThemeSong.uploadFile(mp3_fn, mp3_fn)
    return mp3_fn, song_title


def addFaceInfo(name, userID, cur_img_fn) :
    img_fn = "{}_{}_face.jpg".format(name, userID)
    img_enc_fn = "{}_{}_face_enc.npy".format(name, userID)
    saveEncoding(encode_image(cur_img_fn), img_enc_fn)
    ThemeSong.uploadFile(img_enc_fn, img_enc_fn)
    ThemeSong.uploadFile(cur_img_fn, img_fn)
    return img_fn, img_enc_fn


def addUser(name, yt_url, cur_img_fn) :
    # insert name into table, with time stamp of upload/modify date
    userID = query.sqlAddName(name)
    # song stuff
    mp3_fn, song_title = addSongInfo(name, userID, yt_url)
    # face stuff
    img_fn, img_enc_fn = addFaceInfo(name, userID, cur_img_fn)
    # add users to db 
    query.sqlAddUser(userID, name, yt_url, mp3_fn, song_title, img_fn, img_enc_fn)


def modifyUserSong(name, userID, yt_url) :
    old_mp3_fn = query.sqlGetMP3Name(userID)
    ThemeSong.deleteFile(old_mp3_fn)
    mp3_fn, song_title = addSongInfo(name, userID, yt_url)
    query.sqlModifySong(userID, mp3_fn, song_title, yt_url)


def modifyUserPhoto(name, userID, new_img_fn) :
    old_img = query.sqlGetImgName(userID)
    old_img_enc = query.sqlGetImgEncName(userID)
    ThemeSong.deleteFile(old_img)
    ThemeSong.deleteFile(old_img_enc)
    img_fn, img_enc_fn = addFaceInfo(name, userID, new_img_fn)
    query.sqlModifyFaceImg(userID, img_fn, img_enc_fn)


def deleteUserData(userID) :
    old_img = query.sqlGetImgName(userID)
    old_img_enc = query.sqlGetImgEncName(userID)
    old_mp3_fn = query.sqlGetMP3Name(userID)
    ThemeSong.deleteFile(old_img)
    ThemeSong.deleteFile(old_img_enc)
    ThemeSong.deleteFile(old_mp3_fn)
    query.sqlDeleteRecord(userID)



# addUser("nabil", "https://www.youtube.com/watch?v=9-tfkd9vnnA&ab_channel=ek1", "nabil.jpg")
# addUser("sarim", "https://www.youtube.com/watch?v=V7UgPHjN9qE&ab_channel=DrakeVEVO", "sarim.jpg")
# addUser("taha", "https://www.youtube.com/watch?v=OrYjTUbyLZ4&ab_channel=ChiefKeef-Topic", "taha.jpg")
# modifyUserSong("misbah", "10", "https://www.youtube.com/watch?v=9-tfkd9vnnA&ab_channel=ek1")
# modifyUserPhoto("misbah", 10, "sarim.jpg")
# deleteUserData(10)