class Human:
    def __init__(self, name: str, age: int, gender: str):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.test = 5

    def __str__(self):
        return f'{self.__name}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        if isinstance(new_name, str):
            self.__name = new_name
            return
        raise ValueError('Новое имя должно быть строкой')

    @name.deleter
    def name(self):
        self.__name = 'unknown'


human = Human(name='Олег', age=25, gender='Мужчина')
print(human.name)
del human.name
print(human.name)
