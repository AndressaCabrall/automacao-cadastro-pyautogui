import pyautogui
import time

time.sleep(5)

print(pyautogui.position())

from pytube import YouTube
import os
url = "https://www.youtube.com/watch?v=9olENDPTyxM"

video = YouTube(url)
stream = video.streams.get_highest_resolution()
stream.download()

print("Download concluído!")



