try:
    from . import youtube, reddit, twitter, pinterest, tiktok
except ImportError:
    import youtube, reddit, twitter, pinterest, tiktok
download_functions = {
    'YouTube': youtube.download,
    'Reddit': reddit.download,
    'Twitter': twitter.download,
    'Pinterest': pinterest.download,
    'TikTok': tiktok.download
}