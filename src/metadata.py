import yt_dlp

def get_info(url):
    with yt_dlp.YoutubeDL({"quiet":True}) as ydl:
        info = ydl.extract_info(url, download=False)
        
        return info
