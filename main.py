import urllib3
import os
import sys
import readchar
from bs4 import BeautifulSoup
import page
import search
import wiki_api

host_name = 'https://en.wikipedia.org'
special_search_strt = '/wiki/Special:Search?search='


urllib3.disable_warnings()
http = urllib3.PoolManager()

rows, columns = os.popen('stty size', 'r').read().split()
rows = int(rows)
columns = int(columns)

display_size = rows*columns - 4*columns



def handle_long_output(output_buffer):
    global rows, columns, display_size

    output_buffer = output_buffer.replace('\t', 8*'')
    output_buffer_split = output_buffer.split('\n')
    output_buffer = ''
    for line in output_buffer_split:
        output_buffer += line + ' '*(columns - len(line))


    cmd = '_'
    current_display_ptr = 0
    while cmd != 'q':
        if cmd == ' ' or cmd == '\x1b[B':
            current_display_ptr += columns
        if cmd == '\x1b[A':
            current_display_ptr -= columns
        os.system('clear')
        print(output_buffer[current_display_ptr:current_display_ptr+display_size]+'\n\n')
        if current_display_ptr+display_size >= len(output_buffer):
            break
        print('Press space or down arrow: to move down, up arrow: to move up, and q: quit viewing output')
        sys.stdout.write(':')
        sys.stdout.flush()
        cmd = readchar.readkey()

    if cmd != '_':
        os.system('clear')


if __name__ == '__main__':
    os.system('clear')
    version = '0.0.2.6'
    break_string = '\n\n======================================================================\n\n'

    print(break_string)
    print('Welcome to Wikipedia Command Line Interface(wiki-cli) version '+version)
    print(break_string)


    page_name = input("wikipedia.org$ ")
    while page_name != 'exit':
        (limit, results) = wiki_api.searchQuery(page_name)

        if limit == 1:
            Pg = page.Page(page_name)
            output_str = break_string + Pg.printText() + break_string
            handle_long_output(output_str)

        else:
            SearchObject = search.Search(page_name)
            output_str = break_string+SearchObject.display_next()+break_string
            output_str += 'Could not find such a page top 10 search results are displayed above\n'
            output_str += 'Press right arrow: next 10 results, left arrow: previous 10 results, s: select one of the result, q: quit searching\n'


            handle_long_output(output_str)
            cmd = '_'
            while cmd != 'q':
                cmd = readchar.readkey()
                if cmd == '\x1b[C':
                    output_str = break_string+SearchObject.display_next()+break_string
                    output_str += 'Could not find such a page top 10 search results are displayed above\n'
                    output_str += 'Press right arrow: next 10 results, left arrow: previous 10 results, s: select one of the result, q: quit searching\n'
                    handle_long_output(output_str)

                elif cmd == '\x1b[D':
                    output_str = break_string+SearchObject.display_prev()+break_string
                    output_str += 'Could not find such a page top 10 search results are displayed above\n'
                    output_str += 'Press right arrow: next 10 results, left arrow: previous 10 results, s: select one of the result, q: quit searching\n'
                    handle_long_output(output_str)

                elif cmd == 's':
                    try:
                        idx = int(input("Enter the page search number :: "))
                        Pg = SearchObject.select(idx)
                        output_str = break_string+Pg.printText()+break_string
                        handle_long_output(output_str)
                        break

                    except ValueError:
                        print("Error :: You need to enter an appropriate integer!")


        page_name = input("wikipedia.org$ ")
