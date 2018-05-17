import urllib3
from bs4 import BeautifulSoup
import main

class Page:
    """Holds data section for wikipedia page."""
    def __init__(self, page):
        if isinstance(page, str):
            response = main.http.request('GET', main.host_name+page)
            self.parser = BeautifulSoup(response.data, 'html.parser')
        else:
            self.parser = page

    def printText(self):
        return self.parser.text
