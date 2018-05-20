import requests
import json

api_url = 'https://en.wikipedia.org/w/api.php'
host_name = 'https://en.wikipedia.org/wiki/'


def searchQuery(srsearch, sroffset = 0, srlimit = 10):
    search_query = {'action': 'query', 'list': 'search', 'format': 'json', 'srsearch': srsearch, 'sroffset': sroffset, 'srlimit': srlimit}
    response = requests.get(api_url, params = search_query).json()
    results = response['query']['search']
    limit = response['query']['searchinfo']['totalhits']
    search_results = []
    for result in results:
        search_results.append({'title': result['title'], 'link': host_name+result['title'].replace(' ', '_'), 'pageid': result['pageid']})
    return (limit, search_results)


if __name__ == '__main__':
    search_results = []

    (limit, results) = searchQuery('what is going on here', 0, 100)

    for result in results:
        search_results.append({'title': result['title'], 'link': host_name++result['title'].replace(' ', '_')})

    print(search_results)
