import requests
import pygame
import time

'''
File like object that streams the mp3 file found in the 
presigned url that allows access to mp3 files. 
Provides a mechanism to listen to songs without 
downloading them from AWS S3 buckets
'''
class Stream(object):
    def __init__(self, url):
        self._file = requests.get(url, stream=True)
    def read(self, *args):
        if args:
            return self._file.raw.read(args[0])
        else:
            return self.file.raw.read()
    def close(self):
        self._file.close()


'''
Plays an mp3 file identified by the file name
for a desired amout of time on device speakers
Param :
    fileName : name of mp3 file
    playTime : desired amount of seconds to play song
Returns: none
Effects: plays audio on device speakers 
'''
pygame.init()
pygame.mixer.init()
def playMusic(fileNameUrl, playTime) :
    mp3Stream = Stream(fileNameUrl)
    pygame.mixer.music.load(mp3Stream)
    pygame.mixer.music.play()
    startTime = time.time()
    while True:  
         # plays music for desired amount of time
         curTime = time.time()
         if playTime <= curTime - startTime : 
             break
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
