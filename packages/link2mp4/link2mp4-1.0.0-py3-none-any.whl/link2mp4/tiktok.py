try:
    from .capture import requests, video
except ImportError:
    from capture import requests, video
def download():
    id = input('https://www.tiktok.com/')
    req = requests('https://www.tiktok.com/%s' % id)
    return video(list(filter(lambda req: 'mime_type=video_mp4' in req, req))[0])