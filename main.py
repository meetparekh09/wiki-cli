import urllib3
import os
import sys
import readchar
# from bs4 import BeautifulSoup
# import page
# import search

host_name = 'https://en.wikipedia.org'
special_search_strt = '/wiki/Special:Search?search='


urllib3.disable_warnings()
http = urllib3.PoolManager()

rows, columns = os.popen('stty size', 'r').read().split()
rows = int(rows)
columns = int(columns)

display_size = rows*columns - 3*columns

output_buffer = '\thello world how are you doing?\n'*100


output_buffer = output_buffer.replace('\t', ' '*4)
output_buffer_split = output_buffer.split('\n')
output_buffer = ''
for line in output_buffer_split:
    output_buffer += line + ' '*(columns - len(line))
# output_buffer = []

# for c in output:
    # if c == '\n':
        # output_buffer.append((c, columns))

cmd = '_'
current_display_ptr = 0
while cmd != 'q':
    if cmd == ' ':
        current_display_ptr += columns
    os.system('clear')
    print(output_buffer[current_display_ptr:current_display_ptr+display_size]+'\n\n')
    if current_display_ptr+display_size >= len(output_buffer):
        break
    sys.stdout.write(':')
    sys.stdout.flush()
    cmd = readchar.readkey()

os.system('clear')

# if __name__ == '__main__':
#     os.system('clear')
#     version = '0.0.1.7'
#     break_string = '\n\n======================================================================\n\n'
#
#     print(break_string)
#     print('Welcome to Wikipedia Command Line Interface(wiki-cli) version '+version)
#     print(break_string)
#
#
#     page_name = input("wikipedia.org$ ")
#     while page_name != 'exit':
#         page_name = page_name.replace(' ', '+')
#         response = http.request('GET', host_name+special_search_strt+page_name)
#         parser = BeautifulSoup(response.data, 'html.parser')
#
#         ind = parser.title.text.find('Search results')
#         if ind == -1:
#             Pg = page.Page(parser)
#             print(break_string)
#             print(Pg.printText())
#             print(break_string)
#
#             print('Press q to go back to search mode')
#             cmd = readchar.readkey()
#             while cmd != 'q':
#                 cmd = readchar.readkey()
#         else:
#             SearchObject = search.Search(page_name)
#             print(break_string)
#             print(SearchObject.display_next())
#             print(break_string)
#             print('Could not find such a page top 10 search results are displayed above')
#             print('Press right arrow: next 10 results, left arrow: previous 10 results, s: select one of the result, q: quit searching')
#             cmd = '_'
#             while cmd != 'q':
#                 cmd = readchar.readkey()
#                 if cmd == '\x1b[C':
#                     print(break_string)
#                     print(SearchObject.display_next())
#                     print(break_string)
#                 elif cmd == '\x1b[D':
#                     print(break_string)
#                     print(SearchObject.display_prev())
#                     print(break_string)
#                 elif cmd == 's':
#                     try:
#                         idx = int(input("Enter the page search number :: "))
#                         Pg = SearchObject.select(idx)
#                         print(break_string)
#                         print(Pg.printText())
#                         print(break_string)
#
#                         print('Press q to go back to search mode')
#                         cmd = readchar.readkey()
#                         while cmd != 'q':
#                             cmd = readchar.readkey()
#                         break
#                     except ValueError:
#                         print("Error :: You need to enter an appropriate integer!")
#
#
#         os.system('clear')
#         page_name = input("wikipedia.org$ ")
