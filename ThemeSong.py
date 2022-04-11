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


this_url = "https://www.youtube.com/watch?v=2D-ZO2rGcSA&ab_channel=GamingSoundFX"
play_audio(this_url, 10)
play_all_audio("https://www.youtube.com/watch?v=Mh99q7frpjI&ab_channel=BaraaMasoud%D8%A8%D8%B1%D8%A7%D8%A1%D9%85%D8%B3%D8%B9%D9%88%D8%AF")

