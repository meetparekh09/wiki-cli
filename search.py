import urllib3
from bs4 import BeautifulSoup
import main
import page
import wiki_api


class Search:
    def __init__(self, page):
        self.search_limit = 100
        self.offset = 0
        self.curr_offset = 0
        self.page_name = page
        self.search_results = []

        (self.limit, self.search_results) = wiki_api.searchQuery(self.page_name, self.offset, self.search_limit)


    def display_next(self, num = 10):
        output_str = ''
        while self.curr_offset + num > len(self.search_results):
            self.offset += self.search_limit
            (_, results) = wiki_api.searchQuery(self.page_name, self.offset, self.search_limit)
            self.search_results.extend(results)

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
            (_, results) = wiki_api.searchQuery(self.page_name, ind-1, 1)
            if len(results) == 0:
                print('Your request cannot be satisfied')
                return
            else:
                link = results[0]['link']
                response = main.http.request('GET', link)
                parser = BeautifulSoup(response.data, 'html.parser')
                return page.Page(parser)


        link = self.search_results[ind-1]['link']
        response = main.http.request('GET', link)
        parser = BeautifulSoup(response.data, 'html.parser')
        return page.Page(parser)
