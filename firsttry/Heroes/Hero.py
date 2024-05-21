# class Hero:
#     def __init__(self, name: str, hp: int, armor: int, stamina: int, hero_class: str, temporary_health: int) -> None:
#         if not isinstance(name, str) or not name.isalpha():
#             raise ValueError(f'Атрибут "name" должен быть строкой и состоять только из букв - получено {name}.')
#         if not isinstance(hp, int) or hp <= 0:
#             raise ValueError(f'Атрибут "hp" должен быть указан цифрой и не должен быть меньше "0" - получено {hp}.')
#         if not isinstance(armor, int) or armor <= 0:
#             raise ValueError(f'Атрибут "armor" должен быть указан цифрой и не должен быть меньше "0" - получено {armor}.')
#         if not isinstance(stamina, int) or stamina <= 0:
#             raise ValueError(f'Атрибут "stamina" должен быть указан цифрой и не должен быть меньше "0" - получено {stamina}.')
#         if not isinstance(hero_class, str) or not hero_class.isalpha():
#             raise ValueError(f'Атрибут "hero_class" должен быть строкой и состоять только из букв - получено {hero_class}.')
#
#         self.__name = name
#         self.hp = hp
#         self.__armor = armor
#         self.__stamina = stamina
#         self.__alive = True
#         self.hero_class = hero_class
#         self.temporary_health = temporary_health
#
#     def get_damage(self, damage_value: int):
#         if not isinstance(damage_value, int) or damage_value < 0:
#             raise ValueError(f'Значение "damage_value" должен быть указан цифрой и не должен быть меньше "0" - получено {damage_value}.')
#         self.hp -= damage_value
#         if self.hp <= 0:
#             self.__alive = False
#
#     def get_heal(self, heal_value: int):
#         if not isinstance(heal_value, int) or heal_value < 0:
#             raise ValueError(f'Значение "heal_value" должен быть указан цифрой и не должен быть меньше "0" - получено {heal_value}.')
#         if self.__alive is False:
#             print('Мертвого героя вылечить нельзя...')
#         else:
#             self.hp += heal_value
#
#     def show_hp(self):
#         print(f'Текущее состояние здоровья: {self.hp}.')
#
#     def set_hp(self, hp_value: int):  # сеттер, с помощью которого мы можем переписать изначальное значение HP
#         if not isinstance(hp_value, int) or hp_value <= 0:
#             raise ValueError(f'Атрибут "hp_value" должен быть указан цифрой и не должен быть меньше "0" - получено {hp_value}.')
#         self.hp = hp_value
#
#     def get_hp(self) -> int:  # геттер, с помощью которого можно получить значение для дальнейшей обработки.
#         return self.hp
#
#     # @property
#     # def hp(self) -> int:
#     #     return self.__hp
#     #
#     # @hp.setter
#     # def hp(self, hp_value: int) -> None:
#     #     if not isinstance(hp_value, int) or hp_value <= 0:
#     #         raise ValueError(f'Атрибут "hp_value" должен быть указан цифрой и не должен быть меньше "0" - получено {hp_value}.')
#     #     self.__hp = hp_value
#     #
#     # @hp.deleter
#     # def hp(self):
#     #     print(f'Удаляется свойство hp.')
#     #     del self.__hp
#
#
# class Archer(Hero):
#     def __init__(self, weapon: str, race: str, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.weapon = weapon
#         self.race = race
#
#
# class Mage(Hero):
#     def __init__(self, weapon: str, race: str, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.weapon = weapon
#         self.race = race
#
#
# class Necromancer(Hero):
#     def __init__(self, weapon: str, race: str, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.weapon = weapon
#         self.race = race
#
#
# class Paladin(Hero):
#     def __init__(self, weapon: str, race: str, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.weapon = weapon
#         self.race = race
#
#
# class Priest(Hero):
#     def __init__(self, weapon: str, race: str, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.weapon = weapon
#         self.race = race
#
#
# class Shaman(Hero):
#     def __init__(self, weapon: str, race: str, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.weapon = weapon
#         self.race = race
#
#     def sprout(self, value: int):
#         over_heal = 0
#         if self.hp >= 50_000:
#             print('Лечение не сработало.')
#         else:
#             self.hp += value
#             if self.hp >= 50_000:
#                 over_heal += self.hp - 50_000
#                 print(f'{self.hp} также имеется временное здоровье:{over_heal}')
#
#
# class Mystic(Hero):
#     def __init__(self, stress: int, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.stress = stress
#
#     def scorching(self, damage: int, stress: int) -> list:
#         self.stress = stress
#         return [damage, self.stress]
#
#     def mental_trauma(self, damage: int, stress: int) -> list:
#         self.stress -= stress
#         return [damage, self.stress]
#
#
# class Enemy:
#     def __init__(self, hp: int, armor: int) -> None:
#         self.hp = hp
#         self.armor = armor
#
#
# class Boss(Hero):
#     def __init__(self, energy: int, phase: int,*args, **kwargs) -> None:
#         super().__init__(*args, **kwargs)
#         self.energy = energy
#         self.phase = phase
#
#     def attack(self, damage: int, energy: int) -> list:
#         self.energy -= energy
#         return [damage, self.energy]
#
#     def charge_attack(self, damage: int, energy: int) -> list:
#         self.energy -= energy
#         return [damage, self.energy]
#
#     def stun(self, damage: int, energy: int) -> list:
#         self.energy -= energy
#         return [damage, self.energy]
#
#     def ultimate_attack(self, damage: int, energy: int) -> list:
#         self.energy -= energy
#         for _ in range(3):
#             if self.phase < 3:
#                 damage *= 2
#                 self.phase += 1
#             else:
#                 damage *= 3
#                 self.phase = 0
#         return [damage, self.energy]
#
#
# hero1 = Mystic(stress=5)
#
# enemy1 = Enemy(1800, 75)
# enemy2 = Boss(hp=10000, armor=200, energy=200, phase=0)
#
# hero1.scorching(damage=150, stress=45)
# print(hero1.stress)
#
# shaman = Shaman(weapon='Staff', race='Orc',name='Weakness', hp=50_000, armor=500, stamina=100, hero_class='Shaman',
#                 temporary_health=0)
#
# print(shaman.temporary_health)
# shaman.get_damage(5000)
# print(shaman.get_hp())
# shaman.sprout(10_000)
#
#
class Husband:
    def __init__(self, name: str, wife: 'Wife'):
        self.name = name
        self.wife = wife


class Wife:
    def __init__(self, name: str):
        self.name = name


wife = Wife(name='ANNA')
husband = Husband(name='Drorth', wife=wife)

CON_1 = 1
CON_2 = 2

class Mathematic:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def constantest_method():
        return CON_1*CON_2


kazel = Mathematic(name='Kazel')

print(kazel.constantest_method())
