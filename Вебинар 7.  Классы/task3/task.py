class PublicTransport:
    def __init__(self, brand, engine_power, year, color, max_speed):
        pass
        # todo Здесь нужно написать код

    def info(self):
        """Информация о транспорте"""
        # todo Здесь нужно написать код
        return


class Bus(PublicTransport):
    def __init__(self, brand, engine_power, year, color, max_speed, passengers, car_park, fare):
        super().__init__(brand, engine_power, year, color, max_speed)
        pass
        # todo Здесь нужно написать код

    def park(self):
        """Парк приписки автобуса"""
        # todo Здесь нужно написать код
        return


class Tram(PublicTransport):
    def __init__(self, brand, engine_power, year, color, max_speed, route, path, fare):
        super().__init__(brand, engine_power, year, color, max_speed)
        # todo Здесь нужно написать код

    def how_long(self):
        """Время прохождения маршрута"""
        # todo Здесь нужно написать код
        return
