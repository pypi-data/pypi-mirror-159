from urllib.parse import urlparse
from urllib3 import PoolManager
from m3u8 import loads
try:
    from .capture import requests
except ImportError:
    from capture import requests
def download():
    id = input('https://twitter.com/')
    req = requests('https://twitter.com/%s' % id)
    pool_manager = PoolManager()
    playlist_source = list(filter(lambda req: '.m3u8' in req, req.copy()))[0]
    host = urlparse(playlist_source)
    host_url = '%s://%s' % (host.scheme, host.hostname)
    playlists_text = pool_manager.request('GET', playlist_source).data.decode()
    playlists = loads(playlists_text)
    if playlists.playlists:
        playlists_text = pool_manager.request('GET', host_url + max(playlists.playlists, key=lambda x: x.stream_info.resolution).uri).data.decode()
        playlists = loads(playlists_text)
    return pool_manager.request('GET', host_url + playlists_text[playlists_text.find('"') + 1: playlists_text.rfind('"')]).data + b''.join(map(lambda x: pool_manager.request('GET', host_url + x).data, playlists.segments.uri))