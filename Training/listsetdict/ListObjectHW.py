# Задача 1: Дан список, состоящий из любого количества любых элементов. Нужно убрать все дублирующиеся значения
# в списке (нужно реализовать программу двумя способами - с использованием функции set и без нее)

# any_list = [1, 2, '3', 4, '5', '6', 2, 3, '5', '6']

# Через set
# any_list = list(set(any_list))
#
# print(any_list)

# Без set
# result_list = []
#
# for element in any_list:
#     if element not in result_list:
#         result_list.append(element)
#
# print(result_list)

#
# Задача 2: Дан список состоящий из любого количества целых чисел. Нужно отсортировать этот список по возрастанию
# элементов

# any_list = [1, 250, 515, 324, -4453, 548, 36, 78]
# result_list = []

# for index in range(len(any_list)):
#     possible_min_value = any_list[0]
#     for element in any_list:
#         if element < possible_min_value:
#             possible_min_value = element
#     result_list.append(possible_min_value)
#     any_list.remove(possible_min_value)
# print(result_list)

# МЕТОД ПУЗЫРЬКОВОЙ СОРТИРОВКИ
# for index in range(len(any_list)):
#     for sub_index in range(len(any_list) - 1):
#         if any_list[sub_index] > any_list[sub_index + 1]:
#             any_list[sub_index], any_list[sub_index + 1] = any_list[sub_index + 1], any_list[sub_index]
# print(any_list)

# МЕТОД БИНАРНОГО ПОИСКА
# any_list = [-4453, 1, 36, 78, 250, 324, 515, 548]
# searching_value = 43624362
# value_found = False
#
# while len(any_list) > 1:
#     mid_index = len(any_list) // 2
#     mid_value = any_list[mid_index]
#
#     if searching_value < mid_value:
#         any_list = any_list[:mid_index]
#     elif searching_value > mid_value:
#         any_list = any_list[mid_index:]
#     elif searching_value == mid_value:
#         value_found = True
#         break
#
# if value_found:
#     print('Значение найдено')
# else:
#     print('Такого значения нет')

# Задача 3: Нужно написать программу, которая запрашивает у пользователя ввод строк до тех пор, пока пользователь
# не введет строку "END". После окончания ввода пользователем программа выводит ему список, состоящий из введенных
# строк в порядке возрастания длины этих строк
#
# Например, пользователь вводит:
# <<< Привет
# <<< TextValue
# <<< 512
# <<< True
# <<< END
#
# В таком случае программа выведет пользователю следующий ответ:
# >>> ["512", "True", "Привет", "TextValue"]

# any_string = input('Введите строку: ')
# result_list = []
# 
# while any_string != 'END':
#     result_list.append(any_string)
#     any_string = input('Введите строку: ')
#
# for _ in range(len(result_list)):
#     for index in range(len(result_list) - 1):
#         if len(result_list[index]) > len(result_list[index + 1]):
#             result_list[index], result_list[index + 1] = result_list[index + 1], result_list[index]
#
# print(result_list)
