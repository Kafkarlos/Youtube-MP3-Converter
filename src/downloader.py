import time

from pathlib import Path

from rich.progress import Progress, TextColumn, BarColumn, DownloadColumn 
from rich.console import Console

import yt_dlp

console = Console()

progress = Progress(
    TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    BarColumn(),
    DownloadColumn()
)
task = None

def progress_hook(d):
    global task

    if d['status'] == "downloading":
        total = d.get('total_bytes',0) or d.get('total_bytes_estimate', 0)
        elapsed = d.get('downloaded_bytes',0)
        
        if task is None:
            task = progress.add_task("Baixando",total=total)

        progress.update(
            task,
            completed=elapsed,
        )

    elif d['status'] == "finished":
        progress.update(task, completed=progress.tasks[0].total)
        progress.stop()
        console.print("[yellow]Convertendo mp3...[/]")

def download(url, quality):
    outdir = Path.home()/"Downloads"

    opts = {
        'quiet': True,
        'no_warnings': True,
        'noprogress': True,
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': quality,
        }],
        'progress_hooks': [progress_hook],
        'outtmpl': f'{outdir}/%(title)s.%(ext)s'
    }
    
    console.print("[yellow]Iniciando Download...[/]")

    with progress:
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([url])
    
    console.print("[green]✓ Download Concluído![/]")

