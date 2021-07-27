from bs4.element import ResultSet
from src.driver.pageDownloader import PageDownloader
from src.driver.pageFinder import PageFinder
from typing import List


class Track:
    def __init__(self, page_downloader: PageDownloader) -> None:
        self.page_downloader = page_downloader

    def getStatusTitleList(self) -> List[str]:
        html_content = self.page_downloader.getHtml()
        tag_list = PageFinder.findTags('titulo', html_content)
        result = self.retrieveTitleFromList(tag_list)
        result.reverse()
        return result

    def retrieveTitleFromList(self, tag_list: List[ResultSet]) -> List[str]:
        result = [x.text for x in tag_list]
        return result
