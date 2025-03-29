from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, Location
from keyboards.keyboards import main_kb, end_quiz_kb, end_kb, quiz_kb, make_quiz_option_keyboard, geo_kb
from lexicon.lexicon import LEXICON
from lexicon.censored import make_censored
import requests
from config import FGA_API
from utils.quiz import Quiz
from utils.weather import Weather

router = Router()
#Создаем экземпляр класса Quiz
quiz = Quiz(user="tmp", quiz_theme_dict='geography')

# Хендлер на команду /start
@router.message(Command("start"))
@router.message(F.text == 'Старт')
@router.message(F.text == 'Закончить')
async def process_start_command(message: Message):
    await message.answer(LEXICON['start'], reply_markup=main_kb)

# Хендлер на команду /help
@router.message(Command("help"))
async def process_help_command(message: Message):
    await message.answer(LEXICON['help'])

# Хендлер на команду /random
@router.message(Command("random"))
@router.message(F.text == "Рандомный совет")
@router.message(F.text == "Хочу еще совет")
async def process_random_command(message: Message):
    response = requests.get(FGA_API)
    censored_response = make_censored(response.json()['text'])

    await message.answer(censored_response, reply_markup=end_kb)

# Хендлер на команду /quiz
@router.message(F.text == "Еще вопрос")
@router.message(Command("quiz"))
@router.message(F.text == 'Квиз')
async def process_quiz_command(message: Message):
    quiz.user = message.from_user.username
    await message.answer('Игра в квиз. Выбирай тему', reply_markup=quiz_kb)

@router.message(F.text == 'География')
async def callback_geography(message: Message):
    quiz.quiz_theme_dict = 'geography'
    await message.answer(text=quiz.get_question(), reply_markup=make_quiz_option_keyboard(quiz.get_options()))

@router.message(F.text == 'Наука')
async def callback_geography(message: Message):
    quiz.quiz_theme_dict = 'science'
    await message.answer(text=quiz.get_question(), reply_markup=make_quiz_option_keyboard(quiz.get_options()))

@router.message(F.text == 'Русский рок')
async def callback_geography(message: Message):
    quiz.quiz_theme_dict = 'rock'
    await message.answer(text=quiz.get_question(), reply_markup=make_quiz_option_keyboard(quiz.get_options()))

@router.message(F.text == 'Автомобили')
async def callback_geography(message: Message):
    quiz.quiz_theme_dict = 'auto'
    await message.answer(text=quiz.get_question(), reply_markup=make_quiz_option_keyboard(quiz.get_options()))

@router.message(F.text == 'Показать статистику')
async def show_stat(message: Message):
    await message.answer(text=quiz.show_stat())

# Хендлер на команду /weather
@router.message(Command("weather"))
@router.message(F.text == 'Погода')
async def weather(message: Message):
    await message.answer(text='Поделиться геолокацией (используй свой телефон)', reply_markup=geo_kb)

#Хэндлер на обрабатку геолокации
@router.message(F.location)
async def location_cathed(message: Location):
    weather = Weather(message.location.latitude, message.location.longitude)
    await message.answer(weather.get_weather(), reply_markup=main_kb)

# Хэндлер на все что не обработано и на повторные ответы в квизе
@router.message()
async def not_handled_messages(message: Message):
    if message.text in quiz.get_options():
        text_for_reply = quiz.check_answer(message.text)
        quiz.generate_random()
        await message.answer(text_for_reply, reply_markup=end_quiz_kb)
    else:
        await message.reply(text='Я не знаю такого слова.', reply_markup=main_kb)