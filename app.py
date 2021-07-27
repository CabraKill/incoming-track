from src import app
from src.controllers.statusController import StatusController
from src.driver.pageFinder import PageFinder
from src.handler.track import Track
from src.driver.pageDownloader import PageDownloader
from page import PAGE_LINK

@app.route('/')
def home():
    return "Welcome ^^"

page_downloader = PageDownloader(PAGE_LINK)
track = Track(page_downloader)
status_controller = StatusController(track)

