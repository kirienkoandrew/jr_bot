import requests
from config import WEATHER_TOKEN, WEATHER_API


class Weather:
    """
    Класс объекта погоды
    """
    def __init__(self, lat: float, lon: float):
        self.lat = lat
        self.lon = lon

    #метод обращения к сервису погоды, в ответ получаем json и из него выбираем нужные нам данные, возвращаем их в виду строки
    def get_weather(self):
        request = requests.get(f'{WEATHER_API}?lat={self.lat}&lon={self.lon}&lang=ru&units=metric&appid={WEATHER_TOKEN}')
        response = request.json()
        return (f"Сейчас {response['weather'][0]['description']}, температура {response['main']['temp']} градусов, ощущается как {response['main']['feels_like']}"
                f", ветер {response['wind']['speed']} м/с, населенный пункт {response['name']}")
