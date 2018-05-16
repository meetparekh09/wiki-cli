import urllib3
from bs4 import BeautifulSoup
from page import *

urllib3.disable_warnings() #temporary fix
http = urllib3.PoolManager()

if __name__ == '__main__':
    page_name = input(">>")
    # print(url)
    page_name = page_name.replace(' ', '+')
    # print(page_name)
    page = http.request('GET', 'https://en.wikipedia.org/wiki/Special:Search?search='+page_name)
    # print(page.data)
    parser = BeautifulSoup(page.data, 'html.parser')
    # print(parser.title.text)
    ind = parser.title.text.find('Search results')
    if ind == -1:
        Pg = Page(parser)
        Pg.printText()
    else:
        print('Need to search')
