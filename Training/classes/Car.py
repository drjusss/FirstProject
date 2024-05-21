# # Задача: Написать класс "Car", который будет иметь такие свойства, как
# # wheels - список колес (каждое колесо является объектом класса Wheel)
# # doors - список дверей (каждая дверь является объектом класса Door)
# # motor - двигатель (двигатель является объектом класса Motor)
# #
# # Каждая деталь должна иметь свои свойства и функциональность
# # (например, колесо имеет степень надутости и может лопаться. А дверь имеет свойство открыта/закрыта и может менять это состояние)
# #
# # Таким образом нужно описать функциональный клас машины
#
#
# class Wheel:
#     def __init__(self, diameter: float) -> None:
#         self.diameter = diameter
#
#     @classmethod
#     def bursting(cls):
#         print('Колесо лопнуло!')
#
#     @classmethod
#     def inflate(cls):
#         print('Колесо надувается')
#
#     @classmethod
#     def deflate(cls):
#         print('Колесо сдувается')
#
#
# right_front_wheel = Wheel(diameter=19)
# right_back_wheel = Wheel(diameter=19)
# left_front_wheel = Wheel(diameter=19)
# left_back_wheel = Wheel(diameter=19)
#
#
# class Door:
#     def __init__(self, status: str = 'Закрыта') -> None:
#         self.status = status
#
#     def open(self):
#         print('Дверь открылась.')
#         self.status = 'Открыта'
#
#     def close(self):
#         print('Дверь закрылась.')
#         self.status = 'Закрыта'
#
#     def __str__(self):
#         return f'Дверь {self.status}'
#
#
# # right_front_door = Door(status='Закрыта')
# # right_back_door = Door(status='Закрыта')
# # left_front_door = Door(status='Закрыта')
# # left_back_door = Door(status='Закрыта')
#
#
# class Motor:
#     def __init__(self, motor_power: int) -> None:
#         self.motor_power = motor_power
#         self._hide_motor_power = motor_power
#         self.__private_motor_power = motor_power
#
#
# # right_back_door.open()
# # print(right_back_door.status)
# # right_back_door.close()
# # print(right_back_door.status)
#
#
# class Car:
#     def __init__(self, motor_power: int):
#         self.doors = [Door() for _ in range(4)]
#         self.motor = Motor(motor_power=motor_power)
#
#     def close_all_doors(self):
#         for door in self.doors:
#             # door.status = 'Закрыта'
#             door.close()
#
#     def open_all_doors(self):
#         for door in self.doors:
#             # door.status = 'Открыта'  # Не делать так
#             door.open()
#
#
# car = Car(motor_power=120)
# print(car.motor.motor_power)
# car.motor.motor_power = 'Олег'
# print(car.motor.motor_power)
# print(car.motor._hide_motor_power)
# car.motor._hide_motor_power = 'Олег'
# print(car.motor._hide_motor_power)
#
# print(car.motor._Motor__private_motor_power)
# car.motor._Motor__private_motor_power = 'Олег'
# print(car.motor._Motor__private_motor_power)


