'''
Author: Joshua Noel
Date: 23/12/19
Version: s1e0 (v1.0)
License: GNU General Public License v3.0
'''

from pytube import YouTube
from pytube.helpers import safe_filename
from moviepy.editor import *
import os
import sys

url = ""
fileType = ""

def exit():
	os.system("cls")

	yes = ["Yes", "YES", "yes", "Y", "y"] #possible responses to indicate 'yes'
	no = ["No", "NO", "no", "N", "n"] #possible responses to indicate 'no'

	quit = input("Are you sure you want to quit?\n")

	while (yes.count(quit) != 1) or (no.count(quit) != 1):
		if yes.count(quit) == 1: #checks if anything form the 'yes' list is typed
			os.system("cls")
			sys.exit()

		elif no.count(quit) == 1: #checks if anything form the 'no' list is typed
			main()

		else:
			input("An error has occured, please try again\n")
			exit()

def downloader(fileType, url, yt, stream): #function to download video
	currentDir = os.getcwd() #gets current working directory of script
	location = ""
	vidTitle = ""
	rename = ""

	if fileType == "1":
		stream.download() #downloads video as mp4 to be converted to mp3
		vidTitle = (safe_filename(yt.title)) #gets video title
		location = currentDir + "/{}.mp4".format(vidTitle) #stores location of downloaded mp4
		rename = currentDir + "/{}".format(vidTitle) #prepared a location + name for the converted mp4
		conversion = VideoFileClip(location) #converts mp4 to mp3 
		conversion.audio.write_audiofile("{}.mp3".format(rename)) #writes the converted file to the prepared location
		conversion.close() #closes converter process so that old file can be deleted
		os.remove(location) #deletes old mp4
		print("File successfully downloaded to: {}".format(rename))
		input("Press any key to continue..")

	elif fileType == "2":
		stream.download() #downloads video as mp4
		vidTitle = (safe_filename(yt.title)) #gets video title
		location = currentDir + "/{}.mp4".format(vidTitle) #stores location of downloaded mp4
		print("File successfully downloaded to: {}".format(location))
		input("Press any key to continue..")

	else:
		print("An error has occured")

def main():
	option = ""
	while (option != "."):
		os.system("cls")
		option = input("Please choose an option:\n(1) Download a video\n(2) Exit\n")

		if option == "1":
			os.system("cls")
			url = input("Please enter the video url: \n") #gets url of video
			yt = YouTube("{}".format(url)) #queries YouTube for specified url
			stream = yt.streams.filter(file_extension = "mp4").first() #prepares video to be downloaded
			fileType = input("Please choose a download type:\n(1) Mp3 [audio only]\n(2) Mp4 [video + audio]\n") #chooses file type to save
			downloader(fileType, url, yt, stream)

		elif option == "2":
			exit()

if __name__ == "__main__":
	main()