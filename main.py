import urllib3
from bs4 import BeautifulSoup
from page import *

http = urllib3.PoolManager()

if __name__ == '__main__':
    Pg = Page('https://en.wikipedia.org/wiki/Taj_Mahal')
    Pg.printText()
