from pytube import YouTube
import os

if (os.name == "nt"):
	clear = lambda: os.system("cls")
else:
	clear = lambda: os.system("clear")

clear()

"""
youtube
https://www.youtube.com/shorts/IGvQY07a6g8
https://youtu.be/K7lxu3-_2vw
https://www.youtube.com/watch?v=vSyOk_24Vy0
"""

link = 'https://www.youtube.com/watch?v=vSyOk_24Vy0'
yt = YouTube(link)

stream = yt.streams.get_highest_resolution() # mp4
# stream = yt.streams.filter(only_audio=True).first() # mp3

stream.download()
