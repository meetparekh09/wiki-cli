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

        self.title = self.parser.findAll('h1', {'class': 'firstHeading'})[0]

    def printText(self):
        div = self.parser.findAll('div', {'class': 'mw-parser-output'})
        return div[0].text

    def getSections(self):
        self.sections = []
        headings = self.parser.findAll('h2')

        for heading in headings:
            self.sections.extend(heading.find_all('span', {'class': 'mw-headline'}))


        output = ''
        for section in self.sections:
            output += section.text+'\n'

        return output


    def getNextSection(self):
        output = ''
        content = self.parser.findAll('div', {'class': 'mw-parser-output'})[0]

        while True:
            travel = content

            while travel.name != 'p' and travel.name != 'h2':
                travel = travel.next

            if travel.name == 'p':
                output += travel.text + '\n'
            elif len(travel.find_all('span')) != 0:
                break

            travel.decompose()

        return output

    def getSummary(self):
        output = ''
        output += self.title.text + '\n\n'

        output += self.getNextSection()

        return output
