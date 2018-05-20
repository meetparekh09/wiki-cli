import urllib3
from bs4 import BeautifulSoup
import main

class Page:
    """Holds data section for wikipedia page."""
    def __init__(self, page):
        if isinstance(page, str):
            response = requests.get(main.host_name + page)
            self.parser = BeautifulSoup(response.text, 'html.parser')
        else:
            self.parser = page

        self.title = self.parser.findAll('h1', {'class': 'firstHeading'})[0]
        self.sections = self.getSections()

        self.sectionstitletext = [self.title.text]

        for section in self.sections:
            self.sectionstitletext.append(section.text)

        self.sectionstext = []

        for _ in range(len(self.sectionstitletext)):
            self.sectionstext.append(self.getNextSection())

    def printText(self):
        output = ''
        for i in range(len(self.sectionstitletext)):
            output += self.sectionstitletext[i] + '\n\n' + self.sectionstext[i] + '\n\n\n'

        return output

    def getSections(self):
        sections = []
        headings = self.parser.findAll('h2')

        for heading in headings:
            sections.extend(heading.find_all('span', {'class': 'mw-headline'}))

        return sections


    def getNextSection(self):
        output = ''
        content = self.parser.findAll('div', {'class': 'mw-parser-output'})[0]

        while True:
            travel = content

            if travel is None:
                break
            # print(travel)
            while travel.name != 'p' and travel.name != 'h2':
                travel = travel.next
                if travel is None:
                    return output

            if travel.name == 'p':
                output += travel.text + '\n'
            elif len(travel.find_all('span')) != 0:
                travel.decompose()
                break

            travel.decompose()
        return output
