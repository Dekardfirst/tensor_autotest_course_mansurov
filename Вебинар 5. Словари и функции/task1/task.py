def letter_stat(our_str):
    """Буквенная статистика
    :param our_str: строка
    :return: словарь со статистикой по буквам
    """
    # todo Здесь нужно написать код
    letters_dict = {letter: our_str.count(letter) for letter in set(our_str)}
    return letters_dict

