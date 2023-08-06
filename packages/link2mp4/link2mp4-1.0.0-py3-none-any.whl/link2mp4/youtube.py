try:
    from .capture import requests, video
except ImportError:
    from capture import requests, video
def download():
    id = input('https://www.youtube.com/watch?v=')
    req = requests('https://www.youtube.com/watch?v=%s' % id)
    vid, aud = list(map(lambda url: '&'.join(filter(lambda element: 'range' not in element, url.split('&'))), filter(lambda req: '---' in req and 'generate' not in req, req)))[:2]
    return video(vid, aud)