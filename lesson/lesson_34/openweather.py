import requests
import config


base_url = 'https://api.openweathermap.org/data/2.5/weather'


def get(longitude, latitude, language):
    try:
        data = requests.get(
            base_url,
            params={
                'lat': latitude,
                'lon': longitude,
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
