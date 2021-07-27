import requests


class PageDownloader:
    def __init__(self, link: str) -> None:
        self.link = link

    def getHtml(self, link: str = '') -> str:
        body = (requests.get(link or self.link).content)
        return body
