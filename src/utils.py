def get_duration(secs: int) -> str:
    if not secs:
        return

    mins = secs//60
    rest = str(secs%60).rjust(2,'0')

    return f"{mins}:{rest}"
