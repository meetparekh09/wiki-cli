import requests
import json

# urllib3.disable_warnings()

# http = urllib3.PoolManager()

search_query = {'action':'query', 'list':'search', 'format':'json', 'srsearch':'what is going on here'}
page_name = input('type in page name : ')

search_query['srsearch'] = page_name
host_name = 'https://en.wikipedia.org/w/api.php'


response = requests.get(host_name, params = search_query).json()

print(response['query'])
