from pathlib import Path

import yt_dlp

def download(url, quality):
    outdir = Path.home()/"Downloads"

    opts = {
        'quiet': True,
        'no_warnings': True,
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': quality,
        }],
        'outtmpl': f'{outdir}/%(title)s.%(ext)s'
    }

    print("Fazendo download...")

    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([url])

    print("Download Concluído!")

