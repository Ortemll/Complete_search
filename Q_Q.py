'''Я не особо понял какую из программ поиска нужно дорабатывать, поэтому:
  поиск осуществляется с помощью geosearch (поиск по организациям)
  текст поиска вводится через stdin
'''

from search_func import that_search_func
from requests import get
from PIL import Image
from io import BytesIO

search_server = "https://search-maps.yandex.ru/v1/"
text = input('Введите запрос> ')
search_params = {
    "apikey": 'dda3ddba-c9ea-4ead-9010-f43fbc15c6e3',
    "text": text,
    "lang": "ru_RU",
    "results": 1
}
search_response = get(search_server, params=search_params).json()

organization = search_response["features"][0]
if "CompanyMetaData" in organization["properties"].keys():
    org_address = organization["properties"]["CompanyMetaData"]["address"]
else:
    org_address = organization["properties"]["GeocoderMetaData"]["text"]
point = organization["geometry"]["coordinates"]
org_point = f'{point[0]},{point[1]}'
print(point, org_address)

static_server = "http://static-maps.yandex.ru/1.x/"
spn = that_search_func(point, org_address)
map_params = {
    "ll": org_point,
    "spn": ','.join(map(str, spn)),
    "l": "map",
    "pt": f"{org_point},pm2pnm"
}
response = get(static_server, params=map_params)
print(response.url)
Image.open(BytesIO(response.content)).show()
