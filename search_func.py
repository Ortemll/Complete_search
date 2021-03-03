from requests import get

def that_search_func(point, address, results=10, default_spn=(0.01, 0.01)):
    if isinstance(point, (tuple, list)):
        point = f'{point[0]},{point[1]}'
    elif isinstance(point, str):
        point = point.replace(' ', '')
    spn = default_spn

    geo_server = "https://geocode-maps.yandex.ru/1.x"
    params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": point,
        "results": results,
        "format": 'json'
    }
    response = get(geo_server, params=params).json()

    for obj in response["response"]["GeoObjectCollection"]["featureMember"]:
        if address == obj["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["text"]:
            lower_corner = [float(el) for el in obj["GeoObject"]["boundedBy"]["Envelope"]["lowerCorner"].split()]
            upper_corner = [float(el) for el in obj["GeoObject"]["boundedBy"]["Envelope"]["upperCorner"].split()]
            spn = (abs(lower_corner[0] - upper_corner[0]), abs(lower_corner[1] - upper_corner[1]))
            break

    return spn


if __name__ == '__main__':
    pass