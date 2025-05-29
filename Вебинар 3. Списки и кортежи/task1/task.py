def modification(lst):
    """Изменение списка
    :param lst: список
    :return: преобразованный список
    """
    # todo Здесь нужно написать код
    if len(lst) < 1:
        return lst

    lst[0], lst[-1] = lst[-1], lst[0]
    return lst
