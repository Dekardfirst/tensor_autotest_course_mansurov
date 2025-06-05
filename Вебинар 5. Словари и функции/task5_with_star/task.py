def to_roman(val):
    """Преобразование арабского числа в римское
    :param val: арабское число
    :return: римское число
    """
    # todo Здесь нужно написать код
    roman_dict = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }
    keys = list(roman_dict.keys())
    values = list(roman_dict.values())
    i = len(keys) - 1
    roman_str = ''
    while val != 0:
        if keys[i] <= val:
            roman_str += values[i]
            val -= keys[i]
        else:
            i -= 1
    return roman_str
