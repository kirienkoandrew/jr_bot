from dotenv import load_dotenv,  find_dotenv
import os

# Загружаем переменные окружения из файла .env
load_dotenv(find_dotenv(filename='./.venv/.env'))

BOT_TOKEN = os.getenv("BOT_TOKEN")