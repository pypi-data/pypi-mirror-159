try:
    from .capture import requests, video
except ImportError:
    from capture import requests, video
def download():
    id = input('https://www.reddit.com/r/')
    req = requests('https://www.reddit.com/r/%s' % id)
    vid = max(filter(lambda req: '.mp4' in req and '_audio.mp4' not in req, req))
    try:
        aud = list(filter(lambda req: '_audio.mp4' in req, req))[0]
    except IndexError:
        aud = None
    return video(vid, aud)