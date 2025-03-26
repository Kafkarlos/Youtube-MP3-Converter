import yt_dlp #client para muitos portais de multimídia

# baixa yt_url para o mesmo diretório no qual o script é executado
def download_audio(yt_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([yt_url])

def main():
    print("="*50)
    url = str(input("Informe a url do vídeo a ser convertido: "))
    print("="*50)
    yt_url = url
    download_audio(yt_url)

main()