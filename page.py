import urllib3
from bs4 import BeautifulSoup
from main import http

class Page:
    """Holds data section for wikipedia page."""
    def __init__(self, page):
        if isinstance(page, str):
            page = http.request('GET', page)
            self.parser = BeautifulSoup(page.data, 'html.parser')
        else:
            self.parser = page

    def printText(self):
        print(self.parser.text)
