def max_division_by_3(num):
    """Преобразование числа
    :param num: натуральное число
    :return: другое натуральное число, удовлетворяющее условиям
    """
    # todo Здесь нужно написать код
    digits_str = list(str(num))
    original_sum = sum(int(digit) for digit in digits_str)
    max_num = num

    for i, digit_str in enumerate(digits_str):
        original_digit = int(digit_str)
        for new_digit in range(9, -1, -1):
            if new_digit != original_digit:
                temp_digits = digits_str[:]
                temp_digits[i] = str(new_digit)
                new_sum = original_sum - original_digit + new_digit
                if new_sum % 3 == 0:
                    new_num_str = "".join(temp_digits)
                    if len(new_num_str) == len(str(num)) and int(new_num_str) > max_num:
                        max_num = int(new_num_str)
    return max_num