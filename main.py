import urllib3
from bs4 import BeautifulSoup
import page
import search


host_name = 'https://en.wikipedia.org'
special_search_strt = '/wiki/Special:Search?search='
# search_results = []

urllib3.disable_warnings() #temporary fix
http = urllib3.PoolManager()
#
# search_limit = 100 #default
# offset = 0 #at the start
# curr_offset = 0

if __name__ == '__main__':
    page_name = input(">>")
    # print(url)
    page_name = page_name.replace(' ', '+')
    # print(page_name)
    response = http.request('GET', host_name+special_search_strt+page_name)
    # print(page.data)
    parser = BeautifulSoup(response.data, 'html.parser')
    # print(parser.title.text)
    ind = parser.title.text.find('Search results')
    if ind == -1:
        Pg = page.Page(parser)
        Pg.printText()
    else:
        # search_string = '&limit='+str(search_limit)+'&offset='+str(offset)
        # page = http.request('GET', host_name+page_name+search_string)
        # parser = BeautifulSoup(page.data, 'html.parser')
        #
        # for ind, div in enumerate(parser.find_all('div', {'class': 'mw-search-result-heading'})):
        #     title = div.text
        #     link = div.a['href']
        #     search_results.append({'title': title, 'link': link})
        #     print(str(ind)+' :: '+title)
        SearchObject = search.Search(page_name)
        # for i in range(20):
            # SearchObject.display_next()
        # SearchObject.display_prev()
        # SearchObject.display_prev()
        SearchObject.display_next()
        # SearchObject.display_prev()
        # SearchObject.display_next()
        Pg = SearchObject.select(3)
        Pg.printText()
