def multiplication_chain(num):
    """Цепочка умножений
    :param num: положительное число
    :return: количество перемножений
    """
    # todo Здесь нужно написать код
    count = 0
    while num >=10:
        product = 1
        for digit in str(num):
            product *= int(digit)
        num = product
        count += 1
    return count
