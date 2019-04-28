import requests
from tmp import config
from app.geocoder import Geocoder
from typing import Tuple


class Weather:
    ICON_URL = 'https://yastatic.net/weather/i/icons/blueye/color/svg/'

    def __init__(self, single_moment_data):
        temp = single_moment_data['temp']
        feels = single_moment_data['feels_like']
        self.temp = (str(temp) if temp < 0 else '+' + str(temp) if temp > 0 else '0') + '°'
        self.feels = (str(feels) if feels < 0 else '+' + str(feels) if feels > 0 else '0') + '°'
        self.icon = self.ICON_URL + single_moment_data['icon'] + '.svg'
        self.wind_speed = single_moment_data['wind_speed']
        self.wind_dir = single_moment_data['wind_dir']
        self.pressure = single_moment_data['pressure_mm']
        self.humidity = single_moment_data['humidity']


class DailyForecast:
    def __init__(self, data: dict):
        self.date = data['date']
        self.day = Weather(data['parts']['day_short'])
        self.night = Weather(data['parts']['night_short'])


class Forecast:
    def __init__(self, data: dict):
        self.days = [DailyForecast(day) for day in data['forecasts']]

    def __iter__(self):
        return self.days.__iter__()


class Adapter:
    def get_forecast(self, city_title: str):
        raise NotImplementedError


class YandexWeatherAdapter(Adapter):
    BASE_URL = 'https://api.weather.yandex.ru/v1/forecast'

    def get_forecast(self, city_title: str) -> Tuple[str, Forecast]:
        coords = Geocoder.get_coords(city_title)
        response = requests.get(f'{self.BASE_URL}?lat={coords.latitude}&lon={coords.longitude}&lang=ru_RU',
                                headers={'X-Yandex-API-Key': config.YANDEX_WEATHER_KEY})

        return coords.title, Forecast(response.json())


class OpenWeatherAdapter(Adapter):
    def get_forecast(self, city_title: str):
        raise NotImplementedError
