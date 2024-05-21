# Закончить программу # Пользователь вводит какие-то значения до сих пор пока не введет 'END'. Эти значения должны сохраняться в словарь в следующем формате:
# # {
# # 'int': [...] - Все введённые данные, которые можно интерпретировать как 'int'
# # ...
# # 'str' [...] - Все введённые данные, которые можно интерпретировать как 'str'
# # }
# # int, str, bool, float, None,
# Добавить преобразование типов   - готово

# Написать программу, которая по запросу пользователя выдает количество баллов ученика.(Пользхователь вводит Фамилию, а программа выдает количество баллов.
# При этом регист при написании Фамилии неважен. Данные берутся из импровизированной базы данных в формате словаря. Словарь заранее определён. Если
# такой фамилии в словаре нет - то выводится соответствуающее значение. (Подсказка использовать метод .get)    - готово

# use_scores = {
#     'петров': 150,
#     'иванов': 200,
#     'сидоров': 263,
#     'кравцов': 300,
#     'алексеев': 222
# }
#
# student = input('Введите фамилию студента: ')
#
# print('Результат: ', end='')
# print(use_scores.get(student.lower(), 'Такого студента в списке нет.'))

# if student in use_scores:
#     print(use_scores[student])
# else:
#     print('Такого студента в списке нет.')


# Дан произвольный словарь. Вывести список ключей словаря с уникальнымии значениями.
#
# {
#     'Петров': 100,
#     'Сидоров': 95
# }

# use_scores = {
#     'Петров': 200,
#     'Иванов': 200,
#     'Сидоров': 263,
#     'Кравцов': 300,
#     'Алексеев': 200,
#     'Галкин': 263,
#     'Ургант': 263
# }
# result_list = []
#
# for surname in use_scores:
#     element_is_uniq = True
#
#     for surname2 in use_scores:
#         if surname != surname2 and use_scores[surname] == use_scores[surname2]:
#             element_is_uniq = False
#             break
#
#     if element_is_uniq:
#         result_list.append(surname)
#
# print(result_list)



# Даны 2 словаря. Нужно вернуть словарь, который состоит из элементов, которые есть только в одном из двух словарей.
#Одинаковыми элементами считаются те, у которых одинаковые значения
# dict1 = {
# 'a': 1,
# 'b': 2,
# 'c': 3
# }
# dict2 = {
# 'b': 2,
# 'c': 3
# 'd': 4
#dict_result = {a: 1, c: 4}

# dict1 = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
#     'h': 1
# }
# dict2 = {
#     'e': 2,
#     'g': 3,
#     'd': 4,
# }
# result = dict()
#
# for key1, value1 in dict1.items():
#     if value1 not in dict2.values() and list(dict1.values()).count(value1) == 1:
#         result[key1] = value1
#
# for key2, value2 in dict2.items():
#     if value2 not in dict1.values() and list(dict2.values()).count(value2) == 1:
#         result[key2] = value2
#
# print(result)

# for key1, value1 in dict1.items():
#     if key1 not in dict2:
#         result[key1] = value1
#
# for key2, value2 in dict2.items():
#     if key2 not in dict1:
#         result[key2] = value2
#
# print(result)




# Дан произвольный словарь. нужно вернуть словарь состоящий из элементов изначального словаря, которые являются непустыми вложенными словарями
# dict1 = {
# 'a': {},
# 'b': 2,
# 'c': 3,
# 'd': {
# 'e':1, 'f':2
# },
# 'f': {
#     'a1': 4,
#     'a5': 7
# }
# }
#
# result_dict = dict()
#
# for key, value in dict1.items():
#     if isinstance(value, dict) and value != dict():
#         result_dict[key] = value
#
# print(result_dict)


# Даны 2 произвольных списка. На основе этих списков, нужно составить словарь ключами которого будут элементы первого списка
# а значения второго. (длина списков может быть разной, в этом случае, необходимо чтобы последний элемент имел значение картежа оставшихся элементов второго списка)
# В случае большего количества ключей - все оставшиеся значения принимают значение None(Первый список ключей состоит только из хэшируемых значений)

list_object = ['int', 'float', 'str', 'bool', 'None', None, None, True, False, 'Privet']
second_list_object = [1.2, 2.5, 123, 'Hello']

final_dict = dict()

if len(list_object) > len(second_list_object):
    min_range = len(second_list_object)

    for index in range(len(list_object)):
        current_key = list_object[index]

        if index >= min_range:
            final_dict[current_key] = None
        else:
            final_dict[current_key] = second_list_object[index]

else:
    min_range = len(list_object)

    for index in range(min_range):
        current_key = list_object[index]

        if index == min_range - 1:
            final_dict[current_key] = tuple(second_list_object[index:])
        else:
            final_dict[current_key] = second_list_object[index]

# for index in range(min_range):
#     # print(list_object[index], end='|')
#     # print(second_list_object[index])
#     final_dict[list_object[index]] = second_list_object[index]

print(final_dict)
