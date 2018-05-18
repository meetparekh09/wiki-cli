import requests
import json

# urllib3.disable_warnings()

# http = urllib3.PoolManager()

# search_query = {'action':'query', 'list':'search', 'format':'json', 'srsearch':'what is going on here'}
# page_name = input('type in page name : ')

# search_query['srsearch'] = page_name
api_url = 'https://en.wikipedia.org/w/api.php'
host_name = 'https://en.wikipedia.org/wiki/'


# response = requests.get(host_name, params = search_query).json()

# print(response['query'])


def searchQuery(srsearch, sroffset, srlimit):
    search_query = {'action': 'query', 'list': 'search', 'format': 'json', 'srsearch': srsearch, 'sroffset': sroffset, 'srlimit': srlimit}
    response = requests.get(api_url, params = search_query).json()
    results = response['query']['search']
    search_results = []
    for result in results:
        search_results.append({'title': result['title'], 'link': host_name+result['title'].replace(' ', '_')})
    return search_results


if __name__ == '__main__':
    search_results = []

    (limit, results) = searchQuery('what is going on here', 0, 100)

    for result in results:
        search_results.append({'title': result['title'], 'link': host_name+result['title'].replace(' ', '_')})

    print(search_results)
