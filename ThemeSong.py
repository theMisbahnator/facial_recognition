# import vlc
# import pafy
# import time

from pytube import YouTube
from moviepy.editor import *
import os
import pygame
import time


# used to appload mp4 files to the AWS
# https://medium.com/bilesanmiahmad/how-to-upload-a-file-to-amazon-s3-in-python-68757a1867c6

# figure out how to deal with header information in MongoDB

''' 
Structure of music system: 

There are two components

AWS S3 
- stores all the mp3 files of audio registered in the music systen
- stores all headshot encodings of users in the server
- stores all encoding of images 

MongoDB
- stores name
- stores images url located in aws s3
- stores the the url/name of mp3 file
- stores connection to encoding (or could be stored here)
- stores song title
- stores youtube url
- stores date added
- last modified


Program starts
1) get all encodings and corresponding names from mongo/AWS and store them in an array
2) run the ML script on rasperry pi (the server side should not apply to this)


During modification

Adding New User
- newUser(name, attachAPhoto, urlToDesiredSong)
- add to mongo
- add to AWS S3

Delete User
- deleteUser(name)
- delete entry in mongo
- delete entry data in aws s3

Change Song
- changeSong(name, urlToNewSong)
- modify url/name of mp3, song title, youtube url, last modified in mongo
- add new song to aws s3
- delete current song attached to user in aws s3

Change Photo
- changePhoto(name, newAttachedPhoto)
- modify image url and last modified in mongo
- add new image to aws s3
- delete current image attached to user in aws s3

Commands are accessable through Django and React interface
'''


'''
Converts an MP4 file into an MP3 file within the current directory.
Stores the result in the current directory
'''
def convertToMP3(fileName) :
    video = VideoFileClip("./{}.mp4".format(fileName))
    video.audio.write_audiofile("./{}.mp3".format(fileName))

'''
Used to download new theme songs at the registration of a 
new user or the request to change to a new song from an 
existing user.
Param : 
    url : url link to a song on youtube
Returns: none
Effects: placecs an mp4 audio file from youtube url within current directory
'''
def downloadVideo(url, userName) :
    print("Getting streams...")
    # youtube object contains header info
    yt = YouTube(url)
    # filters for the best audio stream
    print("Filtering streams...")
    someFiltering =  yt.streams.filter(file_extension='mp4')[0]
    if someFiltering != None :
        print("Downloading...")
        someFiltering.download(filename="{}.mp4".format(userName))
        print("Converting to mp3...")
        convertToMP3(userName)
        os.remove("{}.mp4".format(userName))
        print("Done!")
        return
    # failed to download
    print("ERROR: Audio Stream not Found!")


'''
Plays an mp3 file identified by the file name
for a desired amout of time on device speakers
Param :
    fileName : name of mp3 file
    playTime : desired amount of seconds to play song
Returns: none
Effects: plays audio on device speakers 
'''
pygame.mixer.init()
def playMusic(fileName, playTime) :
    pygame.mixer.music.load('{}.mp3'.format(fileName))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  
         # plays music for desired amount of time
         time.sleep(playTime) 
         pygame.mixer.music.stop()
         break
    pygame.mixer.music.unload()


# downloadVideo("https://www.youtube.com/watch?v=ae5iBHnuD0k&ab_channel=Smileyfacey", "doYaLike")
# playMusic("doYaLike", 10)