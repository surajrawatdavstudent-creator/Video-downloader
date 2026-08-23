import yt_dlp    #a library that extract info and downloaded supported media

url = input("YouTube URL :") 

yt_dlp.YoutubeDL(
    {"format" : "bestvideo +bestaudio/best"}
).download([url])