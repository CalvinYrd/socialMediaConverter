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
	res = (None, None)
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
linksFilename = "links"
if (not os.path.exists(linksFilename)):
	open(linksFilename, "w", encoding = "utf8")
	print(f'Un fichier du nom de "{linksFilename}" a été créé')

else:
	newFileContent = ""
	doneLinks = []; linkTypes = {"yt": 0, "ig": 0}

	with open(linksFilename, "r", encoding = "utf8") as file:
		for link in file.readlines():
			src, fullSrc = linkType(link)

			if (link.strip() and src and link not in doneLinks):
				if (not link.startswith("https://")): link = "https://"+link
				doneLinks.append(link)
				linkTypes[src] += 1

	while True:
		try:
			dlType = input(
f"""Vous êtes sur le point de télécharger {linkTypes["yt"]} post(s) Youtube et {linkTypes["ig"]} post(s) instagram. 
Tappez le chiffre correspondant à l'option que vous souhaitez choisir :

1- Télécharger en mp4
2- Télécharger en mp3 (les liens autres que youtube seront téléchargés en mp4)

> """)
			dlType = int(dlType)
			if (dlType < 1 or dlType > 2): raise AssertionError
			clear()
			break

		except (AssertionError, ValueError):
			clear()
			print("Erreur, la valeur que vous avez saisi est incorrecte.\n")
			continue

	doneLinks = []
	with open(linksFilename, "r", encoding = "utf8") as file:
		for link in file.readlines():
			try:
				src, fullSrc = linkType(link)
				output = "downloads"

				if (link.strip() and link not in doneLinks):
					if (src):
						if (not link.startswith("https://")): link = "https://"+link
						doneLinks.append(link)

						if (src == "yt"):
							yt = YouTube(link)

							if (dlType == 1):
								stream = yt.streams.get_highest_resolution() # mp4
								ext = "mp4"

							elif (dlType == 2):
								stream = yt.streams.filter(only_audio=True).first() # mp3
								ext = "mp3"

							title = stream.title
							title = title.split(" ")
							for i in range(len(title)): title[i] = title[i].capitalize()
							title = "".join(title)
							filename = f"{title}.{ext}"

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

					else: newFileContent += link+"\n"

			except:
				newFileContent += link+"\n"

	# clear()
	n = len([line for line in newFileContent.split("\n") if line.strip()])
	print(f"\nRésultat : {colorama.Fore.RED}{n}{colorama.Fore.RESET} lien(s) incorrect(s)")

	with open(linksFilename, "w", encoding = "utf8") as finalFile:
		finalFile.writelines(newFileContent)
