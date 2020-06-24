'''
Author: Joshua Noel
License: MIT
'''

from pytube import YouTube
from pytube.helpers import safe_filename
import pytube
import os
import sys
import subprocess

global url
global platform
global location 

location = os.getcwd() + "\\Downloads" #Location where downloaded videos go

def youtubeDL(): #Downlooder for youtube videos
    subprocess.run(["cls"], shell= True)
    url = input("Please enter the youtube video url:\n")
    fileType = ""

    #exception handling
    try:
        yt = YouTube(url)

    except pytube.exceptions.RegexMatchError:
        input("Invalid url, press any key to continue...")
        youtubeDL()

    except pytube.exceptions.VideoUnavailable:
        input("Invalid url, press any key to continue...")
        youtubeDL()

    except pytube.exceptions.ExtractError:
        input("Invalid url, press any key to continue...")
        youtubeDL()

    except pytube.exceptions.HTMLParseError:
        input("Invalid url, press any key to continue...")
        youtubeDL()   
    
    title = safe_filename(yt.title)

    fileType = input("Please select file type:\n(1) Mp4\n(2) Mp3\n")

    if fileType == "1":
        stream = yt.streams.filter(progressive= True).first() #Downlaods mp4 from url
        stream.download(location)
        input("File saved to '{}', press any key to continue...".format(location + "\\" + title))
        main()

    elif fileType == "2":
        stream = yt.streams.filter(only_audio= True).first() #Downloads mp3 from url
        stream.download(location)
        input("File saved to '{}', press any key to continue...".format(location + "\\" + title))
        main()
    
    else:
        input("An error has occured, press any key to continue...")
        youtubeDL()

    main()


def twitterDL(): #Downlooder for twitter videos
    subprocess.run(["cls"], shell= True)

    main()

def main():
    subprocess.run(["cls"], shell= True)
    platform = input("Please choose a platform to download from (enter 0 to quit):\n(1) Youtube\n(2) Twitter\n")
    subprocess.run(["mkdir", "downloads"], shell= True)

    if platform == "1":
        youtubeDL()
    
    elif platform == "2":
        twitterDL()

    elif platform == "0":
        sys.exit()

    else:
        print("Invalid selection, press any key to continue")
        main()


if __name__ == "__main__":
    main()



