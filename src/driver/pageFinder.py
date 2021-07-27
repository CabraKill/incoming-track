from bs4 import BeautifulSoup


class PageFinder:

    @staticmethod
    def findTags(title: str, html_content: str):
        soup = BeautifulSoup(html_content, 'html.parser')
        result = soup.find_all("p", class_=title)
        return result
