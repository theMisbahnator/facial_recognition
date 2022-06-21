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
- stores all the mp4 files of audio registered in the music systen

MongoDB
- stores all the meta data per entry along with the path to the song in AWS s3

Adding a New entry:
- add meta data to mongoDB
    - name of person
    - location of image of person and file name in AWS S3
- Add raw files to AWS S3
    - user will be asked to upload a photo 
    - user will be asked to provide a url to the theme song
    - photo can just be transfered as a file
    - url will be conveted into mp4 and transferred as such

Modifiying an existing entry
- modified meta data in mongoDB
    - change image or music path based on change
- update AWS S3
    - delete original photo/song attached to entry
    - add new data and transfer it to AWS S3

Delete an entry
- delete meta data from mongoDB
- Delete data that correlates to entry in AWS S3

helper methods

- playing audio
- figuring if an entry has its data dowloaded
- 
'''

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
    # youtube object contains header info
    yt = YouTube(url)
    # filters for the best audio stream
    someFiltering =  yt.streams.filter(file_extension='mp4')[0]
    if someFiltering != None :
        print("Downloading!")
        someFiltering.download(filename=userName)
        return
    # failed to download
    print("ERROR: Audio Stream not Found!")


print("plz help me")




#downloadVideo('https://www.youtube.com/watch?v=u9n7Cw-4_HQ', "poop.mp4")

# video = VideoFileClip("./poop.mp4")
# video.audio.write_audiofile("./poopy.mp3")

pygame.mixer.init()
pygame.mixer.music.load('poopy.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)







# time_to_open_player = 0

# def set_up_audio(url):
#     video = pafy.new(url)
#     best = video.getbestaudio()
#     return vlc.MediaPlayer(best.url)


# def play_audio(url, desired_time):
#     media = set_up_audio(url)
#     media.play()
#     time.sleep(desired_time + time_to_open_player)
#     media.stop()


# def play_all_audio(url):
#     media = set_up_audio(url)
#     media.play()
#     time.sleep(time_to_open_player)
#     while media.is_playing():
#         time.sleep(1)
#     media.stop()