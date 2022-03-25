import requests
import config


base_url = 'https://api.openweathermap.org/data/2.5/weather'


def get_city_id(city, language):
    try:
        data = requests.get(
            base_url,
            params={
                'q': city,
                'type': 'like',
                'units': 'metric',
                'lang': language,
                'appid': config.weather_token
            }).json()
        city_id = data['id']
        return city_id
    except Exception as e:
        return e


def get(city_id, language):
    try:
        data = requests.get(
            base_url,
            params={
                'id': city_id,
                'units': 'metric',
                'lang': language,
                'appid': config.weather_token
            }).json()
        description = data['weather'][0]['description']
        temp = int(data['main']['temp'])
        city = data['name']
        return description, str(temp), city
    except Exception as e:
        return e
