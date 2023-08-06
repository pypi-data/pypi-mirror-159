from moviepy.editor import VideoFileClip, AudioFileClip
from seleniumwire.webdriver import Firefox, Chrome, Edge, Safari
DEBUG = False # change to make the browser visible for debugging
Options = lambda: None # noqa
browsers = {
    'firefox': Firefox,
    'chrome': Chrome,
    'edge': Edge,
    'safari': Safari
}
for browser in browsers:
    try:
        exec("from selenium.webdriver.%s.webdriver import Options" % browser)
        options = Options()
        options.headless = not DEBUG
        browsers[browser](options=options)
    except:
        continue
    break
else:
    raise Exception("No browser found, please install geckodriver")
def requests(url):
    driver = browsers[browser](options=options)
    driver.get(url)
    requests = driver.requests
    driver.quit()
    return list(map(lambda req: req.url, requests))
def video(video, audio=None):
    if audio is None:
        return VideoFileClip(video)
    else:
        return VideoFileClip(video).set_audio(AudioFileClip(audio))