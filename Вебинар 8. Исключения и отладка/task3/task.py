def segment(first_point, second_point):
    """Сумма всех координат точек
    :param first_point: координаты первой точки
    :param second_point: координаты второй точки
    :return: текст исключения наоборот или сумму всех координат
    """
    try:
        x1, y1 = first_point
        x2, y2 = second_point
        total_sum = x1 +y1 + x2 + y2
    except Exception as e:
        return str(e)[::-1]
    else:
        return total_sum
