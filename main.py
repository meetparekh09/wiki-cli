import urllib3
import readchar
from bs4 import BeautifulSoup
import page
import search

host_name = 'https://en.wikipedia.org'
special_search_strt = '/wiki/Special:Search?search='


urllib3.disable_warnings()
http = urllib3.PoolManager()


if __name__ == '__main__':
    version = '0.0.1.5'
    break_string = '\n\n======================================================================\n\n'

    print(break_string)
    print('Welcome to Wikipedia Command Line Interface(wiki-cli) version '+version)
    print(break_string)


    page_name = input("wikipedia.org$ ")
    while page_name != 'exit':
        page_name = page_name.replace(' ', '+')
        response = http.request('GET', host_name+special_search_strt+page_name)
        parser = BeautifulSoup(response.data, 'html.parser')

        ind = parser.title.text.find('Search results')
        if ind == -1:
            Pg = page.Page(parser)
            print(break_string)
            Pg.printText()
            print(break_string)
        else:
            SearchObject = search.Search(page_name)
            print(break_string)
            SearchObject.display_next()
            print(break_string)
            print('Could not find such a page top 10 search results are displayed above')
            print('Press right arrow: next 10 results, left arrow: previous 10 results, q: quit searching')
            cmd = '_'
            while cmd != 'q':
                cmd = readchar.readkey()
                if cmd == '\x1b[C':
                    print(break_string)
                    SearchObject.display_next()
                    print(break_string)
                elif cmd == '\x1b[D':
                    print(break_string)
                    SearchObject.display_prev()
                    print(break_string)

        page_name = input("wikipedia.org$ ")
