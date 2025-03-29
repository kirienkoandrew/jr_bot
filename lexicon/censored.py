def make_censored_word(word: str) -> str:
    """
    Ищет в слове буквы яйёуц и заменяет их на *
    :param word: строка
    :return: строка
    """
    res = ''
    for char in word:
        if char in 'яйёуцех':
            res += '*'
        else:
            res += char
    return res

def make_censored(text: str) -> str:
    """
    Ищет совпадение слова из входной строки со словами из файла ./lexicon/bad_words.txt
    Если слово найдено, слово передается функции make_censored_word,
    Возвращаем строку с "оцензуренным" советом
    :param text: строка
    :return: строка
    """
    with open('./lexicon/bad_words.txt', 'r') as bad_words:
        text_line = bad_words.readlines()
        for t in text_line:
            t.rstrip('\n')
        res = []
        word_lst = list(text.split())
        for text in word_lst:
            if text.rstrip('!,.') in text_line:
                res.append(make_censored_word(text))
            else:
                res.append(text)
        return ' '.join(res)
