def which_triangle(a, b, c):
    """Определение типа треугольника
    :param a: длина стороны
    :param b: длина стороны
    :param c: длина стороны
    :return: тип треугольника
    """
    # todo Здесь нужно написать код

    # Не треугольник
    if a + b <= c or a + c <= b or b + c <= a:
        return 'Не треугольник'

    # Равносторонний
    if a == b == c:
        return 'Равносторонний'

    # Равнобедренный
    if a == b or a == c or b == c:
        return 'Равнобедренный'

    # Обычный
    return 'Обычный'

