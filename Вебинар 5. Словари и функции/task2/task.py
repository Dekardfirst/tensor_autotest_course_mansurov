def repeats(our_str):
    """Повторы букв
    :param our_str: строка
    :return: новая строка с повторами букв
    """
    # todo Здесь нужно написать код
    symbol_counts = {}
    result_str = ""
    for symbol in our_str:
        if symbol in symbol_counts:
            symbol_counts[symbol] += 1
        else:
            symbol_counts[symbol] = 1
        result_str += f"{symbol}_{symbol_counts[symbol]}"
    return result_str

