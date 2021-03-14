r"""
Реализовать базовый класс Worker (работник):
    определить атрибуты: name, surname, position (должность), income (доход);
    последний атрибут должен быть защищённым и ссылаться на словарь,
        содержащий элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
    создать класс Position (должность) на базе класса Worker;
    в классе Position реализовать методы получения  полного имени сотрудника (get_full_name)
                                                    и дохода с учётом премии (get_total_income);
    проверить работу примера на реальных данных:    создать экземпляры класса Position,
                                                    передать данные,
                                                    проверить значения атрибутов,
                                                    вызвать методы экземпляров.
"""


class Worker:
    """Родительский класс"""
    def __init__(self, income=None, inp_name: str = '', inp_surname: str = '', inp_position: str = ''):
        self.name = inp_name
        self.surname = inp_surname
        self.position = inp_position
        self._income = income

    @property
    def income(self):
        """даруем защищённому атрибуту доступ во внешний мир. чтоб пихарм не ругался"""
        return self._income

    def get_params(self):
        """Показать все атрибуты"""
        return self.name, self.surname, self.position, self._income


class Position(Worker):
    """Дочерний класс"""
    def __init__(self, _income, name, surname, pos):
        super().__init__(_income, name, surname, pos)       # присваиваем атрибуты родительского класса

    def get_full_name(self):
        """Метод возврата полного имени"""
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        """Метод возврата дохода"""
        return self._income['wage'] + self._income['bonus']


positions = set()   # множество рабочих позиций

# Создаём работников, переносим их параметры в рабочие позиции, добавляем позиции в множество
worker1 = Worker({'wage': 15000, 'bonus': 200}, 'Василий', 'Петров', 'Инженер')
position1 = Position(worker1.income, worker1.name, worker1.surname, worker1.position)
positions.add(position1)

worker2 = Worker({'wage': 30000, 'bonus': 50000}, 'Марья', 'Иванова', 'Бухгалтер')
position2 = Position(worker2.income, worker2.name, worker2.surname, worker2.position)
positions.add(position2)

worker3 = Worker({'wage': 20000, 'bonus': 1000}, 'Евгений', 'Ларионов', 'Охрана труда')
position3 = Position(worker3.income, worker3.name, worker3.surname, worker3.position)
positions.add(position3)

worker4 = Worker({'wage': 100000, 'bonus': 200000}, 'Инокентий', 'Житомиров', 'Руководитель')
position4 = Position(worker4.income, worker4.name, worker4.surname, worker4.position)
positions.add(position4)

for posit in positions:     # листаем множество вытаскивая из него данные по позициям
    print(f'\nДанные по работнику:\t{posit.get_params()}')
    print(f'Полное имя работника:\t{posit.get_full_name()}')
    print(f'Полный доход работника:\t{posit.get_total_income()}')
