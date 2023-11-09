import requests

api_key = '016b6d19-5e00-4bc8-b2cc-831c0e2ac8d9'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)
