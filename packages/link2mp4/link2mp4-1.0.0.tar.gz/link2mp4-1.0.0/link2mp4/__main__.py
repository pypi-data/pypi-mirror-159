from tkinter import Tk
from tkinter.filedialog import asksaveasfilename
from questionary import select
from os import remove
try:
    from . import download_functions
except ImportError:
    from __init__ import download_functions
def main():
    Tk().withdraw()
    outname = asksaveasfilename(filetypes = [("MP4 file", "*.mp4")])
    website = select("Choose source website", download_functions.keys()).ask()
    if outname == '':
        return
    if not outname.endswith('.mp4'):
        outname += '.mp4'
    try:
        video = download_functions[website]()
        if isinstance(video, bytes):
            with open(outname, 'wb') as f:
                f.write(video)
        else:
            video.write_videofile(outname)
    except KeyError:
        print('Google popped up a captcha. Try again later.')
    except KeyboardInterrupt:
        print('\nCancelled.')
    try:
        remove(outname.rstrip(".mp4") + "TEMP_MPY_wvf_snd.mp3")
    except FileNotFoundError:
        pass
if __name__ == '__main__': main()