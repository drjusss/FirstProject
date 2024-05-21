# # Нужен зоопарк.
# # Где необходимо описать зверей.
# # Описать Как говорят звери.
# # К каждому классу добавить 1 property метод и 1 static метод.
#
#
# # class Animal:
# #     def __init__(self, name: str, age: int, nutrition: str) -> None:
# #         if not name.isalpha():
# #             raise ValueError(f'Имя должно содержать только буквы - получено {name}')
# #         if nutrition.lower() != 'carnivore' and nutrition.lower() != 'herbivorous':
# #             raise ValueError(f'Тип питания для животного должен быть '
# #                              f'"плотоядное" или "травоядное" - получено {nutrition}.')
# #         if not isinstance(age, int) or age < 0 or age > 150:
# #             raise ValueError(f'Возраст должен быть число в диапазоне от 0 до 150 - получено {age}.')
# #
# #         self.name = name
# #         self.age = age
# #         self.nutrition = nutrition.capitalize()
# #
# #     def __str__(self):
# #         return f'Animal(name="{self.name}", age="{self.age}", nutrition="{self.nutrition}")'
# #
# #     def say(self):
# #         print(f'{self.name} издает "звуки".')
# #
# #     @staticmethod
# #     def hello():
# #         print('Hello!')
# #
# #
# # class Cat:
# #     def __init__(self, name: str, age: int, nutrition: str) -> None:
# #         if not name.isalpha():
# #             raise ValueError(f'Имя должно содержать только буквы - получено {name}')
# #         if nutrition.lower() != 'carnivore' and nutrition.lower() != 'herbivorous':
# #             raise ValueError(f'Тип питания для животного должен быть '
# #                              f'"плотоядное" или "травоядное" - получено {nutrition}.')
# #         if not isinstance(age, int) or age < 0 or age > 150:
# #             raise ValueError(f'Возраст должен быть число в диапазоне от 0 до 150 - получено {age}.')
# #
# #         self.name = name
# #         self.age = age
# #         self.nutrition = nutrition.capitalize()
# #
# #     def __str__(self):
# #         return f'Cat(name="{self.name}", age="{self.age}", nutrition="{self.nutrition}")'
# #
# #     def say(self):
# #         print(f'{self.name} говорит "Мяу')
# #
# #     @staticmethod
# #     def hello():
# #         print('Hello!')
# #
# #
# # class Dog:
# #     def __init__(self, name: str, age: int, nutrition: str) -> None:
# #         if not name.isalpha():
# #             raise ValueError(f'Имя должно содержать только буквы - получено {name}')
# #         if nutrition.lower() != 'carnivore' and nutrition.lower() != 'herbivorous':
# #             raise ValueError(f'Тип питания для животного должен быть '
# #                              f'"плотоядное" или "травоядное" - получено {nutrition}.')
# #         if not isinstance(age, int) or age < 0 or age > 150:
# #             raise ValueError(f'Возраст должен быть число в диапазоне от 0 до 150 - получено {age}.')
# #
# #         self.name = name
# #         self.age = age
# #         self.nutrition = nutrition.capitalize()
# #
# #     def __str__(self):
# #         return f'Dog(name="{self.name}", age="{self.age}", nutrition="{self.nutrition}")'
# #
# #     def say(self):
# #         print(f'{self.name} говорит "Гав')
# #
# #     @staticmethod
# #     def hello():
# #         print('Hello!')
# #
# #
# # dog = Dog(name='Anton', age=10, nutrition='Herbivorous')
# # dog.say()
# # cat = Animal(name='Timon', age=7, nutrition='Carnivore')
# # cat.say()
# # cat = Cat(name='Timon', age=7, nutrition='Carnivore')
# # cat.say()
#
#
# # Реализовать почти такую же логику как и с зоопарком (только пусть он будет человеческий).
# # Структура - класс Person
# # будут наследоваться - расы (Азиаты, черные, европейцы)
# # От каждой расы будут наследоваться 2-3 национальности
# # От каждой национальности будет наследоваться "пол".
# # Должен быть хотябы 1 дополнительный метод и хотябы 1 дополнительное свойство
#
#
# class Potato:
#
#     count = 0
#
#     def __init__(self):
#         self.status = 'Семя'
#         self.add_count()
#
#     def grow(self):
#         if self.status == 'Семя':
#             self.status = 'Росток'
#         elif self.status == 'Росток':
#             self.status = 'Зелёная картошка'
#         elif self.status == 'Зелёная картошка':
#             self.status = 'Спелая картошка'
#
#
#     @classmethod
#     def counter(cls):
#         print(f'На основе класса Potato, было создано {cls.count}')
#
#     @classmethod
#     def add_count(cls):
#         cls.count += 1
#
#     @staticmethod
#     def hello():
#         print('Privet')
#
#
# # potato = Potato()
# # # potato2 = Potato()
# #
# # print(potato.status)
# # potato.grow()
# # print(potato.status)
# # potato.grow()
# # print(potato.status)
# # potato.grow()
# # print(potato.status)
# # potato.grow()
# # print(potato.status)
# # potato.counter()
# # potato2 = Potato()
# # potato2.counter()
# # potato.counter()
# # potato.hello()
#
#
# class Animal:
#
#     def __init__(self, name: str, gender: str,  food_type: str, some_property=None, age: int = 10):
#         if not (isinstance(age, int) and age > 0):
#             raise ValueError
#
#         self.age = age
#         self.name = name
#         self.gender = gender
#         self.food_type = food_type
#         self.some_property = some_property
#
#     @staticmethod
#     def say():
#         print('Гаф')
#
# class Cat(Animal):
#     @staticmethod
#     def say():
#         print('Мяу')
#
#     def __init__(self, breed: str, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.breed = breed
#
#
# animal = Animal(name='Тимон', gender='Мужской', food_type='Плотоядный')
# cat = Cat(name='Барсик', gender='Женский', age=11, breed='Сфинкс', food_type='Травоядный')
#
# print(animal.age)
#
# animal.say()
# cat.say()
import random


# Создать класс животных. У животного может быть ИМЯ, ВОЗРАСТ, ПОЛ, ВИД, ЖИВ\НЕЖИВ.
# ВАЖНО: все свойства животных должны быть защищены, т.е. должны быть приватными.
# Нужно добавить минимум по одному методу, для управления свойствами животного.
# Также, нужно добавить инкапсуляцию для этих свойств, чтобы свойство можно было менять напрямую, но с валидацией.
# При удалении объекта животного, животное УМИРАЕТ, но остается в памяти компьютера.


class Animal:
    def __init__(self, name: str, age: int, gender: str, kind: str):
        if not isinstance(age, int) or age < 0:
            raise ValueError('Возраст должен быть указан цифрой, и должен быть не меньше нуля.')

        if not isinstance(name, str) or len(name) == 0:
            raise ValueError('Имя должно быть указано буквами и длина должна быть не меньше 1.')

        if not gender.lower() == 'мужчина' and not gender.lower() == 'женщина':
            raise ValueError('Гендер должен быть указан в формате: "Мужчина" или "Женщина".')

        if kind.lower() not in ['млекопитающее', 'рыба', 'птица']:
            raise ValueError('Вид должен быть одним из списка: млекопитающее, рыба, птица')

        self.__name = name
        self.__age = age
        self.__gender = gender.title()
        self.__kind = kind.title()

    def born(self, name: str):
        if self.__gender != 'Женщина':
            raise ValueError('Рожать могут только женщины.')
        if random.randint(0, 1):
            gender = 'Мужчина'
        else:
            gender = 'Женщина'
        print(f'С днём рождения {name}')

        return Animal(name=name, age=0, gender=gender, kind=self.__kind)

    def __del__(self):
        print(f'Объект {self.__name} был удален')

    def grow_uo(self):
        self.__age += 1

    def show_age(self):
        print(f'Коту {self.__name} {self.__age} лет')


cat = Animal(name='Тимон', age=7, gender='женщина', kind='млекопитающее')

kitty = cat.born(name='Барсик')
kitty2 = cat.born(name='Борис')
kitty3 = cat.born(name='Барсук')

input('Ожидается действие')



