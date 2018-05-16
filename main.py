import urllib3
from bs4 import BeautifulSoup
import page
import search


host_name = 'https://en.wikipedia.org'
special_search_strt = '/wiki/Special:Search?search='

urllib3.disable_warnings()
http = urllib3.PoolManager()


if __name__ == '__main__':
    page_name = input("wikipedia.org$ ")
    page_name = page_name.replace(' ', '+')
    response = http.request('GET', host_name+special_search_strt+page_name)
    parser = BeautifulSoup(response.data, 'html.parser')

    ind = parser.title.text.find('Search results')
    if ind == -1:
        Pg = page.Page(parser)
        Pg.printText()
    else:
        SearchObject = search.Search(page_name)
        SearchObject.display_next()
