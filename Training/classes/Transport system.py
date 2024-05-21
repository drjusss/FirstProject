# Задача: Система Управления Транспортными Средствами
# Вы разрабатываете систему для управления транспортными средствами в компании, занимающейся логистикой.
# Ваша задача — создать базовый класс Vehicle (Транспортное Средство), от которого будут наследоваться классы различных типов транспортных средств
# (например, Car, Truck, и Motorcycle). Используя принципы наследования и полиморфизма, реализуйте функционал, который позволит управлять разными типами транспортных
# средств через единый интерфейс.
#
# Базовый класс Vehicle должен содержать:
# Атрибуты: make (марка), model (модель), и year (год выпуска).
# Метод start(), который выводит сообщение о том, что транспортное средство заведено.
# Метод stop(), который выводит сообщение о том, что транспортное средство остановлено.
# Классы Car, Truck, и Motorcycle:
# Должны наследовать все свойства и методы класса Vehicle.
# Каждый класс должен иметь дополнительные атрибуты, характерные только для данного типа транспортного средства. Например,
# для Truck может быть атрибут cargo_capacity (грузоподъемность).
# Каждый класс должен переопределить метод start(), добавив специфическое для типа транспортного средства сообщение о
# заведении. Например, для Motorcycle метод может выводить сообщение о том, что мотоцикл заведен с использованием ключа.


class Vehicle:
    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year

    @staticmethod
    def start():
        print('Транспортное средство заведено')

    @staticmethod
    def stop():
        print('Транспортное средство остановлено')


class Car(Vehicle):
    def __init__(self, weight: float, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.weight = weight

    @staticmethod
    def start():
        print('Машина заведена с кнопки "Start"')


class Truck(Vehicle):
    def __init__(self, cargo_capacity: float, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.cargo_capacity = cargo_capacity

    @staticmethod
    def start():
        print('Грузовик со скрежетом завелся')


class Motorcycle(Vehicle):
    def __init__(self, engine_power: float, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.engine_power = engine_power

    @staticmethod
    def start():
        print('Мотоцикл заведен с использованием ключа')


car = Car(make='Mitsubisi', model='Lancer', year=2007, weight=2.2)
truck = Truck(make='MEGATRUCK', model='Truckster', year=2015, cargo_capacity=20.5)
motorcycle = Motorcycle(make='Kawasaki', model='Ninja H2', year=2022, engine_power=900)

motorcycle.start()