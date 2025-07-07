class RomanNums:
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def __init__(self, roman_num):
        self.roman_num = roman_num

    def from_roman(self):
        """Перевод римской записи числа в арабскую"""
        result = 0
        i = 0
        while i < len(self.roman_num):
            if i + 1 < len(self.roman_num) and RomanNums.roman_map[self.roman_num[i]] < RomanNums.roman_map[self.roman_num[i + 1]]:
                result += RomanNums.roman_map[self.roman_num[i + 1]] - RomanNums.roman_map[self.roman_num[i]]
                i += 2
            else:
                result += RomanNums.roman_map[self.roman_num[i]]
                i += 1
        return result

    def is_palindrome(self):
        """Является ли число палиндромом """
        arabic_num = str(self.from_roman())
        return arabic_num == arabic_num[::-1]
