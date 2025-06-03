def josephus_task(num_people, kill_num):
    """Задача Иосифа Флавия
    :param num_people: количество воинов
    :param kill_num: номер воина
    :return: номер последнего оставшегося воина
    """
    # todo Здесь нужно написать код
    warriors = list(range(1, num_people + 1))
    warrior_kill_index = 0

    while len(warriors) > 1:
        index_to_kill = (warrior_kill_index + kill_num - 1) % len(warriors)
        warriors.pop(index_to_kill)
        warrior_kill_index = index_to_kill
    return warriors[0]
