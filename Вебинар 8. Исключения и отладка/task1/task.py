def treatment_sum(our_tuple):
    """Обработка суммы элементов кортежа
    :param our_tuple: кортеж
    :return: сумму элементов кортежа
    """
    # todo Здесь нужно написать код
    try:
        if len(our_tuple) < 2:
            return 'Недостаточно данных'
        if len(our_tuple) > 2:
            raise Exception('Много данных')

        result = our_tuple[0] + our_tuple[1]
        return result
    except TypeError:
        return 'Нельзя сложить эти данные'



