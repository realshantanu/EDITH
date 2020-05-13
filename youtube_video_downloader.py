from pytube import YouTube


video_url = input("Enter Link Of Youtube Video:  ")

yt = YouTube(video_url).streams.first().download("C:\\Users\\Shantanu\\Downloads\\youtube")