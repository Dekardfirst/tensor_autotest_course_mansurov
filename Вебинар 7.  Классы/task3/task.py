class PublicTransport:
    def __init__(self, brand, engine_power, year, color, max_speed):
        self.brand = brand
        self._engine_power = engine_power
        self.year = year
        self.color = color
        self.max_speed = max_speed

    @property
    def info(self):
        """Информация о транспорте"""
        return f"Марка: {self.brand}, Цвет: {self.color}, Год выпуска: {self.year}, Мощность двигателя: {self._engine_power}"


class Bus(PublicTransport):
    def __init__(self, brand, engine_power, year, color, max_speed, passengers, car_park, fare):
        super().__init__(brand, engine_power, year, color, max_speed)
        self.passengers = passengers
        self.__park = car_park
        self._fare = fare

    @property
    def park(self):
        """Парк приписки автобуса"""
        return self.__park

    @park.setter
    def park(self, value):
        """Установка номера парка с проверкой диапазона"""
        assert 1000 <= value <= 9999, "Номер парка должен быть в диапазоне от 1000 до 9999"
        self.__park = value

    @property
    def info(self):
        return f"{super().info()}, Пассажиров: {self.passengers}, Стоимость проезда: {self._fare}, Парк: {self.park}"



class Tram(PublicTransport):
    def __init__(self, brand, engine_power, year, color, max_speed, route, path, fare):
        super().__init__(brand, engine_power, year, color, max_speed)
        self.__route = route
        self.path = path
        self._fare = fare

    @property
    def how_long(self):
        """Время прохождения маршрута"""
        return self.max_speed / (4 * self.path)

    @property
    def route(self):
        """Возвращаем номер маршрута"""
        return self.__route

    @route.setter
    def route(self, value):
        """Устанавливаем номер маршрута"""
        self.__route = value

    @property
    def info(self):
        return f"{super().info()}, Маршрут: {self.__route}, Длина маршрута: {self.path}, Стоимость проезда: {self._fare}"

