def everything_for_your_cat(cats_data):
    """Котики и их владельцы
    :param cats_data: информация о котах и их владельцах
    :return: информация о котах и их владельцах в виде строки
    """
    # todo Здесь нужно написать код
    owners_data = {}
    for cat_name, cat_age, owner_name, owner_surname in cats_data:
        owner_key = f"{owner_name} {owner_surname}"
        owners_data.setdefault(owner_key, []).append(f"{cat_name}, {cat_age}")
    result = ""
    for owner, cats in owners_data.items():
        result += f"{owner}: {'; '.join(cats)}\n"
    return result
