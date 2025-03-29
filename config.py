from dotenv import load_dotenv
import os

# Загружаем переменные окружения из файла .env
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
TOKEN_OPENAI = os.getenv('TOKEN_OPENAI')
WEATHER_TOKEN = os.getenv('WEATHER_TOKEN')

FGA_API = 'https://fucking-great-advice.ru/api/random'
WEATHER_API = 'https://api.openweathermap.org/data/2.5/weather'