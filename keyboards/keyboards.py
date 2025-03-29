from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Основная клавиатура
main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Старт"), KeyboardButton(text="Рандомный совет")],
        [KeyboardButton(text="Квиз"), KeyboardButton(text="Погода")],
    ],
    resize_keyboard=True
)

#Клавиатура при отображении совета
end_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Закончить'), KeyboardButton(text='Хочу еще совет')],
    ],
    resize_keyboard=True
)

#Клавиатура после принятия ответа на вопросы квиза
end_quiz_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Закончить'), KeyboardButton(text='Еще вопрос'), KeyboardButton(text='Показать статистику')],
    ],
    resize_keyboard=True
)

#Клавиатура на выбор темы квиза
quiz_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='География'), KeyboardButton(text='Наука')],
        [KeyboardButton(text='Русский рок'), KeyboardButton(text='Автомобили')]
    ],
    resize_keyboard=True
)


def make_quiz_option_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
    """
    Создаёт реплай-клавиатуру с кнопками в один ряд с вариантами ответов на вопрос
    :param items: список текстов для кнопок
    :return: объект реплай-клавиатуры
    """
    row = [KeyboardButton(text=item) for item in items]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)

#кнопка отправить геолокацию
geo_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Отправить свою геолокацию', request_location=True)]
    ],
resize_keyboard=True
)