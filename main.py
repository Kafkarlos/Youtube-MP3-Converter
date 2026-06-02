from pathlib import Path
import argparse

import yt_dlp

from InquirerPy import inquirer

def download(url, quality):
    opts = {
        'quiet': True,
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': quality,
        }],
        'outtmpl': f'{Path.home()/"Downloads"}/%(title)s.%(ext)s'
    }
    print("Fazendo Download...")

    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([url])

    print("Download Concluído!")

def get_duration(secs: int):
    mins = secs//60
    rest = str(secs%60).rjust(2,"0")

    return f"{mins}:{rest}"

def show_info(url):
    opts = {
        "quiet": True
    }

    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=False)

        print(f"Título: {info.get('title')}")
        print(f"Canal: {info.get('channel')}")
        
        duration = info.get('duration')
        if duration:
            print(f"Duração: {get_duration(info.get('duration'))}")

def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('url', nargs="?", type=str)
    parser.add_argument(
        "--quality",
        help="Qualidade do áudio (kbps)",
        choices=[128,192,320],
        type=int
    )

    args = parser.parse_args()
    
    url = inquirer.text(
        message="URL:",
    ).execute() if not args.url else args.url

    show_info(url)

    confirm = input("Prosseguir com o Download? [S/n]:").lower()
    
    if not confirm or confirm == "s":
        quality = inquirer.select(
            message="Escolha a qualidade (Kbps)",
            choices= [128,192,320],
            vi_mode=True
        ).execute() if not args.quality else args.quality

        download(url, quality)
    else:
        return

if __name__ == '__main__':
    main()

