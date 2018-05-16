import urllib3
from bs4 import BeautifulSoup
from main import http

class Page:
    """Holds data section for wikipedia page."""
    def __init__(self, url):
        self.page = http.request('GET', url)
        self.parser = BeautifulSoup(self.page.data, 'html.parser')

    def printText(self):
        print(self.parser.text)
