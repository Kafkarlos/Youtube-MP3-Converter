import argparse

from InquirerPy import inquirer

from metadata import get_info
from downloader import download
from utils import get_duration

def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('url', nargs="?", type=str)
    parser.add_argument(
        "--quality",
        help="Qualidade do áudio (kbps)",
        choices=[128,192,320],
        type=int
    )
    parser.add_argument('--confirm', action='store_true')
    parser.add_argument('--no-info', action='store_true')

    args = parser.parse_args()

    url = inquirer.text(
        message="URL:",
    ).execute() if not args.url else args.url

    if not args.no_info:
        info = get_info(url)
        print(f"{info.get('channel')} - {info.get('title')}")
        print(f"Duração: {get_duration(info.get('duration'))}")

    if not args.confirm:
        confirm = input("Prosseguir com o Download? [S/n]:").lower()
        if not confirm or confirm == "s":
            pass
        else:
            return
        
    quality = inquirer.select(
        message="Escolha a qualidade (Kbps)",
        choices= [128,192,320],
        vi_mode=True
    ).execute() if not args.quality else args.quality

    download(url, quality)

if __name__ == '__main__':
    main()

