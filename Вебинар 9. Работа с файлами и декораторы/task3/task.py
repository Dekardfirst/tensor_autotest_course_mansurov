def memorize(function):
    """
    Декоратор для кэширования результатов функции
    """
    cache = {}
    def wrapper(*args):
        """
        Оборачивающая функция
        """
        args_tuple = args
        if args_tuple in cache:
            return function(*args), cache
        else:
            result = function(*args)
            cache[args_tuple] = result
            return result, cache
    return wrapper

# todo Здесь ничего изменять не нужно!
@memorize
def get_kinetic_energy(weight, speed):
    """Кинетическая энергия
    :param weight: масса
    :param speed: скорость
    :return: кинетическую энергию
    """
    return (weight * speed ** 2)/2

