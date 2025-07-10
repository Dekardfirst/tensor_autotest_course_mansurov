import pathlib

def three_most_expensive_purchases():
    """Три самые дорогие покупки
    :return: сумму трех самых дорогих покупок
    """
    file_path = "test_file/task_2.txt"
    # todo Здесь нужно написать код
    purchases = []
    current_purchase = []
    most_expensive_purchases = 0

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        current_purchase.append(float(line))
                    except ValueError:
                        print(f"Некорректный формат цены: {line}")
                else:
                    if current_purchase:
                        purchases.append(sum(current_purchase))
                    current_purchase = []
            if current_purchase:
                purchases.append(sum(current_purchase))

        purchases.sort(reverse=True)

        top_3_purchases = purchases[:3]

        most_expensive_purchases = sum(top_3_purchases)

        return most_expensive_purchases

    except FileNotFoundError:
        return 0

    except Exception:
        return 0
