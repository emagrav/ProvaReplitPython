from __future__ import unicode_literals
import youtube_dl as ydl
import urllib
import shutil

print("************YOUTUBE DOWNLOAD********")
ydl_opts={}
with ydl.YoutubeDL(ydl_opts) as ydl:
  ydl.download(["https://www.youtube.com/watch?v=meRN4Fohndk&ab_channel=Ro%D1%8Fschach"])