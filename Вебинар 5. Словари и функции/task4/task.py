def scrabble(word):
    """Игра 'Эрудит'
    :param word: слово
    :return: количество очков за слово
    """
    # todo Здесь нужно написать код
    points_dict = {
        1: ['а', 'в', 'е', 'ё', 'и', 'н', 'о', 'р', 'с', 'т'],
        2: ['д', 'к', 'л', 'м', 'п', 'у'],
        3: ['б', 'г', 'ь', 'я'],
        4: ['й', 'ы'],
        5: ['ж', 'з', 'х', 'ц', 'ч'],
        8: ['ф', 'ш', 'э', 'ю'],
        10: ['щ'],
        15: ['ъ']
    }
    total_points = 0
    for letter in word:
        for points, letters in points_dict.items():
            if letter in letters:
                total_points += points
                break
    return total_points

