#OOP - программирование основанное на объектах.
from datetime import date
import typing


class Person:
    amount_of_objects = 0

    def __init__(self, name: str, age: int, gender: str) -> None:  # Dunder method(Инициализатор) - прописать логику перед создание объекта.
        if not isinstance(age, int) or age < 0 or age > 150:
            raise ValueError(f'Возраст должен быть число в диапазоне от 0 до 150 - получено {age}.')
        if gender.lower() != 'male' and gender.lower() != 'female':
            raise ValueError(f'Пол должен быть равен "Male" или "Female" - получено {gender}.')
        if not name.isalpha():
            raise ValueError(f'Имя должно содержать только буквы - получено {name}')

        self.calculate_amount_of_objects()
        self.name = name
        self.age = age
        self.gender = gender.capitalize()

    def __str__(self) -> str:  # При интерпритации в строку
        return f'Person(name="{self.name}", age="{self.age}", gender="{self.gender}")'

    def __eq__(self, other: typing.Any) -> bool:  # При сравнении
        return False

    @property  # Когда нужно использовать свойство а не метод.
    def year_of_birthday(self):
        current_year = date.today().year
        result = current_year - self.age
        return result

    @classmethod
    def calculate_amount_of_objects(cls):  # cls - идентично 'self', но является ссылко на класс( тут - на весь Person)
        cls.amount_of_objects += 1

    @classmethod
    def show_amount_of_objects(cls):
        print(cls.amount_of_objects)

    def greetings(self):
        print(f'Привет,  меня зовут {self.name}, мне {self.age} лет.')

    def hello(self, name: str):
        print(f'Привет, {name} меня зовут {self.name}.')

    @staticmethod  # Когда метод не связан с объектом.
    def good_bye():
        print('Good bye.')


# Person.show_amount_of_objects()
# human = Person(name='Andrey', age=35, gender='maLe')
# Person.show_amount_of_objects()
# human2 = Person(name='Alexandra', age=43, gender='femaLe')

# Person.show_amount_of_objects()
# human3 = Person(name='Viktoria', age=18, gender='femaLe')
# Person.show_amount_of_objects()

# ********Паттерны ООП*********
# ЭТО БАЗА. Содержит 3 паттерна:
# 1) Наследование.
# 2) Полиморфизм
# 3) Инкапсуляция - сокрытие данных.


# class Animal:
#     def __init__(self, name: str) -> None:
#         self.name = name
#
#     def say(self):
#         print(f'{self.name} издает звуки дикого животного.')
#
#     def sleep(self):
#         print(f'{self.name} крепко уснул.')
#
#
# class Cat(Animal):
#     def drink_milk(self):
#         print(f'{self.name} обжираловка')
#
#     def say(self):
#         print(f'{self.name} сказал "Мяу"')
#
#
# animal = Animal(name='Timon')
# animal2 = Cat(name='Dog')
#
# animal.say()
# animal2.say()
# animal2.drink_milk()
# animal2.sleep()

# class Animal:
#     def __init__(self, name: str, age: int, nutrition: str) -> None:
#         if not name.isalpha():
#             raise ValueError(f'Имя должно содержать только буквы - получено {name}')
#         if nutrition.lower() != 'carnivore' and nutrition.lower() != 'herbivorous':
#             raise ValueError(f'Тип питания для животного должен быть '
#                              f'"плотоядное" или "травоядное" - получено {nutrition}.')
#         if not isinstance(age, int) or age < 0 or age > 150:
#             raise ValueError(f'Возраст должен быть число в диапазоне от 0 до 150 - получено {age}.')
#
#         self.name = name
#         self.age = age + 1
#         self.nutrition = nutrition.capitalize()
#
#     def __str__(self):
#         return f'Animal(name="{self.name}", age="{self.age}", nutrition="{self.nutrition}")'
#
#     def say(self):
#         print(f'{self.name} издает "звуки".')
#
#     def sleep(self):
#         print(f'{self.name} крепко уснул.')
#
#
# class Cat(Animal):
#     def __init__(self, color_of_collar: str, *args, **kwargs) -> None:
#         super().__init__(*args, **kwargs)  # Функция super - возвращает класс "родитель"
#         self.color_of_collar = color_of_collar
#
#     def say(self):  # Полиморфизм - один метод, но в разных классах работает по разному.
#         super().say()
#         print('Которые похожи на "Мяу"')
#
#
# class Dog(Animal):
#     def say(self):
#         print(f'{self.name} говорит "Гав"')
#
#
# animal = Animal(name='Timon', age=7, nutrition='Carnivore')
# dog = Dog(name='Anton', age=10, nutrition='Herbivorous')
# cat = Cat(name='Timon', age=7, nutrition='Carnivore', color_of_collar='Pink')
#
# print(animal.age)
# cat.say()

# class Hero:
#     def __init__(self, name: str, hp: int, armor: int, stamina: int) -> None:
#         if not isinstance(name, str) or not name.isalpha():
#             raise ValueError(f'Атрибут "name" должен быть строкой и состоять только из букв - получено {name}.')
#         if not isinstance(hp, int) or hp <= 0:
#             raise ValueError(f'Атрибут "hp" должен быть указан цифрой и не должен быть меньше "0" - получено {hp}.')
#         if not isinstance(armor, int) or armor <= 0:
#             raise ValueError(f'Атрибут "armor" должен быть указан цифрой и не должен быть меньше "0" - получено {armor}.')
#         if not isinstance(stamina, int) or stamina <= 0:
#             raise ValueError(f'Атрибут "stamina" должен быть указан цифрой и не должен быть меньше "0" - получено {stamina}.')
#
#         self.__name = name
#         self.__hp = hp
#         self.__armor = armor
#         self.__stamina = stamina
#         self.__alive = True
#
#     def get_damage(self, damage_value: int):
#         if not isinstance(damage_value, int) or damage_value < 0:
#             raise ValueError(f'Значение "damage_value" должен быть указан цифрой и не должен быть меньше "0" - получено {damage_value}.')
#         self.__hp -= damage_value
#         if self.__hp <= 0:
#             self.__alive = False
#
#     def get_heal(self, heal_value: int):
#         if not isinstance(heal_value, int) or heal_value < 0:
#             raise ValueError(f'Значение "heal_value" должен быть указан цифрой и не должен быть меньше "0" - получено {heal_value}.')
#         if self.__alive is False:
#             print('Мертвого героя вылечить нельзя...')
#         else:
#             self.__hp += heal_value
#
#     def show_hp(self):
#         print(f'Текущее состояние здоровья: {self.__hp}.')
#
#     # def set_hp(self, hp_value: int):  # сеттер, с помощью которого мы можем переписать изначальное значение HP
#     #     if not isinstance(hp_value, int) or hp_value <= 0:
#     #         raise ValueError(f'Атрибут "hp_value" должен быть указан цифрой и не должен быть меньше "0" - получено {hp_value}.')
#     #     self.__hp = hp_value
#     #
#     # def get_hp(self) -> int:  # геттер, с помощью которого можно получить значение для дальнейшей обработки.
#     #     return self.__hp
#     @property
#     def hp(self) -> int:
#         return self.__hp
#
#     @hp.setter
#     def hp(self, hp_value: int) -> None:
#         if not isinstance(hp_value, int) or hp_value <= 0:
#             raise ValueError(f'Атрибут "hp_value" должен быть указан цифрой и не должен быть меньше "0" - получено {hp_value}.')
#         self.__hp = hp_value
#
#     @hp.deleter
#     def hp(self):
#         print(f'Удаляется свойство hp.')
#         del self.__hp
#
#
# hero = Hero(name='Andrey', hp=100, armor=50, stamina=75)
# hero.get_damage(damage_value=20)
# hero.show_hp()
# hero.get_heal(heal_value=30)
# hero.show_hp()
# print(hero.hp)
# del hero.hp
# hero.hp = 100
# print(hero.hp)


# setter и getter и deleter - set: установить, get: получить. delet: удалить.

# ***Множественное наследование***


# class DriveSkillMixin:  # Для миксинов, всегда указываем в нейминге MIXIN в конце названия класса.
#     @staticmethod
#     def drive():
#         print('Водит машину')
#
#
# class Person:
#     amount_of_objects = 0
#
#     def __init__(self, name: str, age: int, gender: str) -> None:
#         if not isinstance(age, int) or age < 0 or age > 150:
#             raise ValueError(f'Возраст должен быть число в диапазоне от 0 до 150 - получено {age}.')
#         if gender.lower() != 'male' and gender.lower() != 'female':
#             raise ValueError(f'Пол должен быть равен "Male" или "Female" - получено {gender}.')
#         if not name.isalpha():
#             raise ValueError(f'Имя должно содержать только буквы - получено {name}')
#
#         self.name = name
#         self.age = age
#         self.gender = gender.capitalize()
#
#
# class AfroAmerican(Person, DriveSkillMixin):
#     def __init__(self, *args, **kwargs) -> None:
#         super().__init__(*args, **kwargs)
#         self.skin_color = 'Black'
#         self.skill = 'Basketball'
#
#
# class European(Person):
#     def __init__(self, *args, **kwargs) -> None:
#         super().__init__(*args, **kwargs)
#         self.skin_color = 'White'
#         self.hair_color = 'Ginger'
#
#
# class BlackBaby(AfroAmerican):
#     def __init__(self, toy: str, *args, **kwargs) -> None:
#         super().__init__(*args, **kwargs)
#         self.toy = toy
#
#
# class WhiteBaby(European):
#     def __init__(self, toy: str, *args, **kwargs) -> None:
#         super().__init__(*args, **kwargs)
#         self.toy = toy
#
#
# class HybridBaby(AfroAmerican, European):  # При множественном наследовании работает правило приоритетности(то что указано первым - того свойство и будет)
#     def __init__(self, toy: str, *args, **kwargs) -> None:
#         super().__init__(*args, **kwargs)
#         self.toy = toy
#
#
# baby1 = HybridBaby(name='Andrean', toy='Gun', gender='Male', age=18)
# print(baby1.hair_color)
# print(baby1.skill)


# Мексины - доп надстройка для класса(дополнительная функциональность в классу. В первую очередь указываем основные классы для наследования
# далее основной миксин и далее неосновные миксины, чтобы по приоритетности при конфликте остался именно основной.


# ***Внешние библиотеки***

