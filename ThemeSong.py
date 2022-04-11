import vlc
import pafy
import time

time_to_open_player = 5


def set_up_audio(url):
    video = pafy.new(url)
    best = video.getbestaudio()
    return vlc.MediaPlayer(best.url)


def play_audio(url, desired_time):
    media = set_up_audio(url)
    media.play()
    time.sleep(desired_time + time_to_open_player)
    media.stop()


def play_all_audio(url):
    media = set_up_audio(url)
    media.play()
    time.sleep(time_to_open_player)
    while media.is_playing():
        time.sleep(1)
    media.stop()