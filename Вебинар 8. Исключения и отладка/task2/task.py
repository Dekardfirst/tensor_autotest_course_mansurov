class Trigon:
    def __init__(self, *args):
        """
        Инициализация класса Trigon.
        Проверяет корректность переданных данных и генерирует исключения.
        """
        if len(args) != 3:
            raise IndexError(f'Передано {len(args)} аргументов, а ожидается 3')

        self.sides = []
        for side in args:
            if not isinstance(side, (int, float)):
                raise TypeError('Стороны должны быть числами')
            if side <= 0:
                raise ValueError('Стороны должны быть положительными')
            self.sides.append(side)

        a, b, c = self.sides
        if not (a + b > c and a + c > b and b + c > a):
            raise Exception('Не треугольник')


