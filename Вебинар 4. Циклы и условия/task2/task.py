def flatten_and_sort(array):
    """Преобразование двумерного массива в плоский список
    :param array: двумерный массив
    :return: плоский список
    """
    # todo Здесь нужно написать код
    flattened_list = []
    for sublist in array:
        flattened_list.extend(sublist)

    flattened_list.sort()
    return flattened_list