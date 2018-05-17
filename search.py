import urllib3
from bs4 import BeautifulSoup
import main
import page


class Search:
    def __init__(self, page):
        self.search_limit = 100
        self.offset = 0
        self.curr_offset = 0
        self.page_name = page
        self.search_results = []

        search_string = '&limit='+str(self.search_limit)+'&offset='+str(self.offset)

        response = main.http.request('GET', main.host_name+main.special_search_strt+self.page_name+search_string)
        parser = BeautifulSoup(response.data, 'html.parser')

        for div in parser.find_all('div', {'class': 'mw-search-result-heading'}):
            title = div.text
            link = div.a['href']
            self.search_results.append({'title': title, 'link': link})


    def display_next(self, num = 10):
        output_str = ''
        while self.curr_offset + num > len(self.search_results):
            self.offset += self.search_limit
            search_string = '&limit='+str(self.search_limit)+'&offset='+str(self.offset)

            response = main.http.request('GET', main.host_name+main.special_search_strt+self.page_name+search_string)
            parser = BeautifulSoup(response.data, 'html.parser')

            for div in parser.find_all('div', {'class': 'mw-search-result-heading'}):
                title = div.text
                link = div.a['href']
                self.search_results.append({'title': title, 'link': link})

        for i in range(self.curr_offset, self.curr_offset+num):
            output_str += str(i+1)+' :: '+self.search_results[i]['title']+'\n'

        self.curr_offset += num
        return output_str


    def display_prev(self, num = 10):
        output_str = ''
        if self.curr_offset - num < 0:
            return output_str

        for i in range(self.curr_offset-num, self.curr_offset):
            output_str += str(i+1)+' :: '+self.search_results[i]['title']+'\n'

        self.curr_offset -= num
        return output_str


    def select(self, ind):
        if ind >= len(self.search_results):
            search_string = '&limit='+str(1)+'&offset='+str(ind-1)
            response = main.http.request('GET', main.host_name+main.special_search_strt+self.page_name+search_string)
            parser = BeautifulSoup(response.data, 'html.parser')
            headings = parser.find_all('div', {'class': 'mw-search-result-heading'})
            if len(headings) == 0:
                print('Your request cannot be satisfied')
                return
            else:
                link = headings[0].a['href']
                response = main.http.request('GET', main.host_name+link)
                parser = BeautifulSoup(response.data, 'html.parser')
                return page.Page(parser)


        link = self.search_results[ind-1]['link']
        response = main.http.request('GET', main.host_name+link)
        parser = BeautifulSoup(response.data, 'html.parser')
        return page.Page(parser)
