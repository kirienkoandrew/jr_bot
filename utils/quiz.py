from random import choice
from typing import Any


def make_dct(file_name: str) -> dict[int | Any, list[str | list[str]]]:
    """
    Функция получает на вход имя файла, открывает его, считывает данные, генерирует словарь
    :param file_name: имя файла
    :return: словарь с вопросами, списком вариантов ответов и правильным ответом, индекс число от 0
    """
    with open(f'./utils/{file_name}.txt') as file:
        input_dct = {}
        res = {}
        tmp_lst = file.readlines()
        id = 0

        for line in tmp_lst:
            a, b = line.split('Варианты ответов:')
            input_dct[id] = a.lstrip('Вопрос:'), b
            id += 1

        for k, val in input_dct.items():
            options, true = val[1].split('Правильный ответ: ')
            res[k] = [val[0].lstrip(), list(i.lstrip() for i in options.split('; ')), true.rstrip('\n').lstrip(';  ')]
        return res

class Quiz:
    """
    Класс для игы в квиз
    """
    def __init__(self, user: str, quiz_theme_dict: dict[str]):
        """
        user: имя пользователя, берется из message
        quiz_theme_dict: тема для игры в квиз
        user_statistic: словарь статистики
        line: рандомный элемент словаря в виде списка, [0] - сам вопрос, [1] - список вариантов ответов, [2] - правильный ответ
        """
        self.user = user
        self.quiz_theme_dict = quiz_theme_dict
        self.user_statistic = {'true_answer' : 0, 'false_answers' : 0}
        self.line = self.generate_random()

    #геттер имени пользователя
    @property
    def user(self):
        return self._user

    #сеттер имени пользователя
    @user.setter
    def user(self, value):
        if value is None:
            self._user = 'tmp'
        self._user = value

    #геттер темы квиз
    @property
    def quiz_theme_dict(self):
        return self._quiz_theme_dict

    #сеттер темы квиз
    @quiz_theme_dict.setter
    def quiz_theme_dict(self, file_name):
        if file_name is None:
            self._quiz_theme_dict = {}
        elif file_name in ('science', 'geography', 'rock', 'auto'):
            self._quiz_theme_dict = make_dct(file_name)
        else:
            raise ValueError('Нет такого файла')

    #метод возвращает случайный элемент словаря
    def generate_random(self):
        self.line = self.quiz_theme_dict[choice(list(self.quiz_theme_dict))]
        return self.line

    #возвращает вопрос
    def get_question(self):
        return self.line[0]

    #возвращает список вариантов ответов
    def get_options(self):
        return self.line[1]

    #возарвщает правильный ответа
    def get_true_answer(self):
        return self.line[2]

    #метод проверки правильности ответа
    def check_answer(self, text: str) -> str:
        if text == self.get_true_answer():
            self.user_statistic['true_answer'] += 1
            return f'Это правильный ответ'
        else:
            self.user_statistic['false_answers'] += 1
            return f'Это неправильный ответ. Правильный ответ {self.get_true_answer()}'

    #метод отображает количество правильных и неправильных ответов
    def show_stat(self):
        return f'Правильных ответов: {self.user_statistic['true_answer']}, Неправильных ответов: {self.user_statistic['false_answers']}'
