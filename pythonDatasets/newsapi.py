import requests

api_key = '806d0711afd945b49777cb5aeafb6a04'

base_url = 'https://newsapi.org/v2/'

endpoint = 'everything'

search_query = 'Biden'  

params = {
    'apiKey': api_key,
    'q': search_query,  
    'language': 'en',  
}

response = requests.get(base_url + endpoint, params=params)

if response.status_code == 200:
    data = response.json()

    for article in data['articles']:
        print('Title:', article['title'])
        print('Description:', article['description'])
        print('URL:', article['url'])
        print('-' * 30)
else:
    print('Error:', response.status_code)