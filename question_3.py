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
    def __init__(self, inp_name: str = '', inp_surname: str = '', inp_position: str = '', income=None):
        self.name = inp_name
        self.surname = inp_surname
        self.position = inp_position
        self._income = income

    @property
    def income(self):
        """даруем защищённому атрибуту доступ во внешний мир. чтоб пихарм не ругался"""
        return self._income

    def get_params(self):
        """Запросить все атрибуты"""
        return self.name, self.surname, self.position, self._income


class Position(Worker):
    """Дочерний класс"""
    def get_full_name(self):
        """Метод возврата полного имени"""
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        """Метод возврата дохода"""
        return self._income['wage'] + self._income['bonus']


workers = list()    # список работников
positions = list()  # список рабочих позиций

# Создаём работников
workers.append(Worker('Василий', 'Петров', 'Инженер', {'wage': 15000, 'bonus': 200}))
workers.append(Worker('Марья', 'Иванова', 'Бухгалтер', {'wage': 30000, 'bonus': 50000}))
workers.append(Worker('Евгений', 'Ларионов', 'Охрана труда', {'wage': 20000, 'bonus': 1000}))
workers.append(Worker('Инокентий', 'Житомиров', 'Руководитель', {'wage': 100000, 'bonus': 200000}))

# Переносим их параметры в рабочие позиции
for worker in workers:
    positions.append(Position(*worker.get_params()))

for posit in positions:     # листаем список вытаскивая из него данные по позициям
    print(f'\nДанные по работнику:\t{posit.get_params()}')
    print(f'Полное имя работника:\t{posit.get_full_name()}')
    print(f'Полный доход работника:\t{posit.get_total_income()}')
