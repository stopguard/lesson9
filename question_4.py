r"""
Реализуйте базовый класс Car:
    у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
                             А также методы: go, stop, turn(direction),
                             которые должны сообщать, что машина поехала, остановилась, повернула (куда);
    опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
    добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
    для классов TownCar и WorkCar переопределите метод show_speed.
        При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
"""
from random import randint, choice


class Car:
    """Родительский класс авто"""
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        """Старт авто со случайной скоростью"""
        self.speed = randint(20, 80)
        return f'Машина {self.name} поехала.'

    def stop(self):
        """Остановка авто"""
        self.speed = 0
        return f'Машина {self.name} остановилась.'

    def turn(self, direction: str):
        """Поворот авто"""
        return f'Машина {self.name} повернула {direction}.'

    def show_speed(self):
        """Показать скорость авто"""
        return f'Скорость автомобиля {self.name} равна: {self.speed}'


class TownCar(Car):
    """Дочерний класс - городское авто"""
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        """Проверка скорости авто"""
        alarm = '. Внимание! Превышение скорости!' if self.speed > 60 else '.'
        return f'Скорость автомобиля {self.name} равна: {self.speed}{alarm}'


class SportCar(Car):
    """Дочерний класс - спортивное авто"""
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    """Дочерний класс - грузовик"""
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        """Проверка скорости авто"""
        alarm = '. Внимание! Превышение скорости!' if self.speed > 40 else '.'
        return f'Скорость автомобиля {self.name} равна: {self.speed}{alarm}'


class PoliceCar(Car):
    """Дочерний класс - полицейское авто"""
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


# создаём экземпляры
t_car = TownCar(0, 'red', 'Taz', False)
s_car = SportCar(0, 'yellow', 'Porshe', False)
w_car = WorkCar(0, 'orange', 'MAN', False)
p_car = PoliceCar(0, 'blue', 'Skoda', True)
cars_set = {t_car, s_car, w_car, p_car}

# выводим атрибуты и результаты работы методов пока не будет отправлена пустая строка
flag = True
while flag:
    for car in cars_set:
        print(f'\n{car.speed}', end=', ')
        print(car.color, end=', ')
        print(car.name, end=', ')
        print(car.is_police)
        print(car.go())
        print(car.turn(choice(('направо', 'налево'))))
        print(car.show_speed())
        print(car.stop())
    flag = input('\nПопробовать с новыми значениями?\nДля выхода оставьте поле пустым\n>>>')
