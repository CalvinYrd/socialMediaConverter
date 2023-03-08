from pytube import YouTube
import os, instaloader, colorama

# fonction pour clear le terminal
if (os.name == "nt"):
	clear = lambda: os.system("cls")
else:
	clear = lambda: os.system("clear")

clear()

# retourne le réseau social du lien, si celui-ci est parmis les réseaux sociaux acceptés
def linkType(link):
	link = link.lstrip("https://").lstrip("http://").lstrip("www.")
	res = None
	if (
		link.startswith("instagram.com/reel/") and
		(
			link.split("/")[-1].startswith("?igshid=") or
			link.split("/")[-1].startswith("&igshid=")
		)
	): res = ("ig", "INSTAGRAM")
	elif (
		link.startswith("youtube.com/watch?v=") or
		link.startswith("youtube.com/shorts/") or
		link.startswith("youtu.be/")
	): res = ("yt", "YOUTUBE")
	return res

# si le fichier links n'existe pas on le créé
filename = "links"
if (not os.path.exists(filename)):
	with open(filename, "w", encoding = "utf8") as file: pass
	print(f'Un fichier du nom de "{filename}" a été créé')

else:
	newFileContent = ""
	doneLinks = []

	with open(filename, "r", encoding = "utf8") as file:
		for link in file.readlines():
			try:
				src, fullSrc = linkType(link)
				output = "downloads"

				if (link.strip() and src and link not in doneLinks):
					if (not link.startswith("https://")): link = "https://"+link
					doneLinks.append(link)

					if (src == "yt"):
						yt = YouTube(link)
						stream = yt.streams.get_highest_resolution() # mp4

						title = stream.title
						title = title.split(" ")
						for i in range(len(title)): title[i] = title[i].capitalize()
						title = "".join(title)
						filename = f"{title}.mp4"

						print(fullSrc)
						stream.download(
							output_path = output,
							filename=filename
						)
						print((output+"/"+filename).replace("/", "\\"))

					elif (src == "ig"):
						code = link.split("instagram.com/reel/")[-1].split("/")[0]
						ig = instaloader.Instaloader()
						post = instaloader.Post.from_shortcode(ig.context, code)

						print(fullSrc)
						ig.download_post(
							post = post,
							target = output
						)
						for dl in os.listdir(output):
							if (dl.endswith(".jpg") or dl.endswith(".json.xz")):
								os.remove(output+"/"+dl)

			except:
				newFileContent += link+"\n"

	clear()
	n = len([line for line in newFileContent.split("\n") if line.strip()])
	print(f"Résultat : {colorama.Fore.RED}{n}{colorama.Fore.RESET} lien(s) incorrect(s)")

	with open(filename, "w", encoding = "utf8") as finalFile:
		finalFile.writelines(newFileContent)

"""
# youtube
# https://www.youtube.com/shorts/IGvQY07a6g8
# https://youtu.be/K7lxu3-_2vw
# https://www.youtube.com/watch?v=vSyOk_24Vy0

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
