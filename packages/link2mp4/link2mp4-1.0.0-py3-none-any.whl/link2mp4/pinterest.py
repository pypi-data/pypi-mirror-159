try:
    from .capture import requests, video
except ImportError:
    from capture import requests, video
def download():
    id = input('https://www.pinterest.com/pin/')
    req = requests('https://www.pinterest.com/pin/%s' % id)
    return video(list(filter(lambda req: 'v.pinimg' in req, req))[0])