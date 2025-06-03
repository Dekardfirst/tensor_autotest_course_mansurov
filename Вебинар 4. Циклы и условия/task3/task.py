def sum_digits(num):
    """Нахождение суммы цифр числа
    :param num: число
    :return: сумма цифр числа
    """
    # todo Здесь нужно написать код
    summa = 0
    for digit in str(num):
        summa += int(digit)
    return summa

