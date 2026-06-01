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
    }
    print("Fazendo Download...")

    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([url])

    print("Download Concluído!")

def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('url', nargs="?", type=str)
    args = parser.parse_args()
    
    if not args.url:
        print("[bold white on red] Buscar Musica [/]")

        url = inquirer.text(
            message="URL:",
        ).execute()

    else:
        url = args.url

    get_info(url)

    quality = inquirer.select(
        message="Escolha a qualidade (Kbps)",
        choices= [128,192,320],
        vi_mode=True
    ).execute()

    download(url, quality)

def get_duration(secs: int):
    mins = secs//60
    rest = str(secs%60).rjust(2,"0")

    return f"{mins}:{rest}"

def get_info(url):
    opts = {
        "quiet": True
    }

    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=False)

        print(f"Título: {info.get('title')}")
        
        duration = info.get('duration')
        if duration:
            print(f"Duração: {get_duration(info.get('duration'))}")
        
        print(f"Canal: {info.get('channel')}")

if __name__ == '__main__':
    main()

