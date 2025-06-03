from unicodedata import digit


def create_phone_number(num_tuple):
    """Создание номера телефона
    :param num_tuple: кортеж из цифр
    :return: строку в виде номера телефона
    """
    # todo Здесь нужно написать код
    digits_str = [str(digit) for digit in num_tuple]
    area_code = "".join(digits_str[0:3])
    prefix = "".join(digits_str[3:6])
    line_number = "".join(digits_str[6:10])
    return f"({area_code}) {prefix}-{line_number}"
