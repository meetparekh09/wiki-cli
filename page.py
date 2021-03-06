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


        self.removelist = ['External links', 'See also', 'Notes', 'Further reading']

        self.title = self.parser.findAll('h1', {'class': 'firstHeading'})[0]
        self.sections = self.getSections()

        self.sectionstitletext = [self.title.text]

        for section in self.sections:
            self.sectionstitletext.append(section.text)

        self.sectionstext = []

        for _ in range(len(self.sectionstitletext)):
            self.sectionstext.append(self.getNextSection())

        for item in self.removelist:
            if item in self.sectionstitletext:
                self.sectionstitletext.remove(item)

        self.sectionstext = [x for x in self.sectionstext if x != '']
        self.sectionstext.append(self.getReferences())

        try:
            idx = self.sectionstitletext.index('Gallery')
            del self.sectionstitletext[idx]
            del self.sectionstext[idx]
        except:
            return

    def printText(self):
        output = ''
        print(len(self.sectionstext), len(self.sectionstitletext))
        for i in range(len(self.sectionstitletext)):
            output += '\n\n' + self.sectionstitletext[i] + '\n\n' + self.sectionstext[i] + '\n\n\n'

        return output

    def getSections(self):
        sections = []
        headings = self.parser.findAll('h2')

        for heading in headings:
            sections.extend(heading.find_all('span', {'class': 'mw-headline'}))

        return sections

    def getReferences(self):
        spans = self.parser.findAll('span', {'class': 'reference-text'})
        spanText = ''

        for span in spans:
            spanText += span.text + '\n'

        return spanText


    def getNextSection(self):
        output = ''
        content = self.parser.findAll('div', {'class': 'mw-parser-output'})[0]

        while True:
            travel = content

            if travel is None:
                break
            # print(travel)
            while travel.name != 'p' and travel.name != 'h2' and travel.name != 'h3':
                travel = travel.next
                if travel is None:
                    return output

            if travel.name == 'p':
                output += travel.text + '\n'
            elif travel.name == 'h3':
                output += '\n' + travel.text + '\n\n'
            elif len(travel.find_all('span')) != 0:
                travel.decompose()
                break

            travel.decompose()
        return output
