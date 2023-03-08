from pytube import YouTube
import os, instaloader

if (os.name == "nt"):
	clear = lambda: os.system("cls")
else:
	clear = lambda: os.system("clear")

clear()
link = 'https://www.instagram.com/reel/CmBJpVaP3VO/?igshid=YmMyMTA2M2Y='

def linkType(link):
	link = link.lstrip("https://").lstrip("http://").lstrip("www.")
	res = None
	if (
		link.startswith("instagram.com/reel/") and
		(
			link.split("/")[-1].startswith("?igshid=") or
			link.split("/")[-1].startswith("&igshid=")
		)
	): res = "ig"
	elif (

	)

"""
# youtube
# https://www.youtube.com/shorts/IGvQY07a6g8
# https://youtu.be/K7lxu3-_2vw
# https://www.youtube.com/watch?v=vSyOk_24Vy0

src = "youtube"
yt = YouTube(link)

stream = yt.streams.get_highest_resolution() # mp4
ext = "mp4"

stream = yt.streams.filter(only_audio=True).first() # mp3
ext = "mp3"

title = stream.title
"""

# Insta
# https://www.instagram.com/reel/CmBJpVaP3VO/?igshid=YmMyMTA2M2Y=

##############
# cas youtube
"""
title += " "+src
title = title.split(" ")
for i in range(len(title)): title[i] = title[i].capitalize()
title = "".join(title)

filename = f"{title}.{ext}"
output = f"downloads"
"""
##############

"""
# youtube
stream.download(
	output_path = output,
	filename=filename
)
"""

"""
# insta
code = link.split("instagram.com/reel/")[-1].split("/")[0]
ig = instaloader.Instaloader()
post = instaloader.Post.from_shortcode(ig.context, code)

ig.download_post(
	post = post,
	target = output
)

# garder que le mp4
"""
