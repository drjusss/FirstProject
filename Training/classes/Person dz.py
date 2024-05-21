# Реализовать почти такую же логику как и с зоопарком (только пусть он будет человеческий).
# Структура - класс Person
# будут наследоваться - расы (Азиаты, черные, европейцы)
# От каждой расы будут наследоваться 2-3 национальности
# От каждой национальности будет наследоваться "пол".
# Должен быть хотябы 1 дополнительный метод и хотябы 1 дополнительное свойство


class Person:
    amount_of_objects = 0

    def __init__(self, name: str, age: int, gender: str) -> None:
        if not isinstance(age, int) or age < 0 or age > 150:
            raise ValueError(f'Возраст должен быть число в диапазоне от 0 до 150 - получено {age}.')
        if gender.lower() != 'male' and gender.lower() != 'female':
            raise ValueError(f'Пол должен быть равен "Male" или "Female" - получено {gender}.')
        if not name.isalpha():
            raise ValueError(f'Имя должно содержать только буквы - получено {name}')

        self.name = name
        self.age = age
        self.gender = gender.capitalize()


class Asian(Person):
    def __init__(self, weight: int, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.weight = weight

    def stereotype(self):
        print(f'{self.name} отлично разбирается в технике.')


class Black(Person):
    def __init__(self, height: int, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.height = height

    def stereotype(self):
        print(f'{self.name} умеет играть на бас гитаре')


class European(Person):
    def __init__(self, hair_length: int, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.hair_length = hair_length

    def stereotype(self):
        print(f'{self.name} профессиональный сноб')


class Vietnamese(Asian):
    def __init__(self, driver_license: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.driver_license = driver_license

    def attitude_towards_animals(self):
        print(f'{self.name} любят животных :)')


class Chinese(Asian):
    def __init__(self, profession: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.profession = profession

    def attitude_towards_animals(self):
        print(f'{self.name} либо вкладываются в их содержание, либо их едят...')


class Japanese(Asian):
    def __init__(self, standard_of_living: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.standard_of_living = standard_of_living

    def attitude_towards_animals(self):
        print(f'{self.name} относятся к собакам как к верным и преданным друзьям.')


class American(Black):
    def __init__(self, favorite_music: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.favorite_music = favorite_music

    def sport_stereotype(self):
        print(f'{self.name} профессиональный баскетболист.')


class Nigerian(Black):
    def __init__(self, natural_muscles: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.natural_muscles = natural_muscles

    def sport_stereotype(self):
        print(f'{self.name} профессиональный бегун.')


class AfroLatinos(Black):
    def __init__(self, dance_style: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.dance_style = dance_style

    def sport_stereotype(self):
        print(f'{self.name} профессиональный танцор.')


class Russian(European):
    def __init__(self, impudence: str, *args, **kwargs) -> None:  # Impudence - наглость :))
        super().__init__(*args, **kwargs)
        self.impudence = impudence

    def alcoholism_level(self):
        print(f'{self.name} нереальный пьяница')


class German(European):
    def __init__(self, mustache_length: int, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.mustache_length = mustache_length

    def alcoholism_level(self):
        print(f'{self.name} в меру уверенный в себе пьяница')


class Frenchman(European):
    def __init__(self, cultural_level: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.cultural_level = cultural_level

    def alcoholism_level(self):
        print(f'{self.name} неимоверный винный эстет.')


class AsianWoman1(Vietnamese):
    def __init__(self, hair_color: str, *args, ** kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.hair_color = hair_color

    def beauty_saloon(self):
        print(f'{self.name} регулярно посещают салоны красоты')


class AsianWoman2(Chinese):
    def __init__(self, hair_color: str, *args, ** kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.hair_color = hair_color

    def beauty_saloon(self):
        print(f'{self.name} регулярно посещают салоны красоты')
