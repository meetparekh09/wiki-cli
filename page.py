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
        div = self.parser.findAll('div', {'class': 'mw-parser-output'})
        return div[0].text

    def getSections(self):
        sections = []
        headings = self.parser.findAll('h2')

        print(headings)

        for heading in headings:
            sections.extend(heading.find_all('span', {'class': 'mw-headline'}))

        print(sections)

        output = ''
        for section in sections:
            output += section.text+'\n'

        return output
