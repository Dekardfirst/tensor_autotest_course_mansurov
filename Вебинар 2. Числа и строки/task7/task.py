def minimum_length_slice(first_string, second_string):
    """Срез минимальной длины
    :param first_string: первая строка
    :param second_string: вторая строка
    :return: min_slice срез минимальной длины строки second_string
    """
    # todo Здесь нужно написать код
    indices = [second_string.find(char) for char in first_string]

    if -1 in indices:
        return ""

    min_index = min(indices)
    max_index = max(indices)

    min_slice = second_string[min_index : max_index + 1]
    return min_slice
