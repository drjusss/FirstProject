# Нам дан список состоящий из строк. Необходимо отсортировать данный список, в порядке возрастания длины строк и Алфавита.

# any_list = ['ABC', 'erhg4reh', 'Brerg', 'ABCDEFG', 'Hello', 'World']
#
#
# for _ in range(len(any_list)):
#     for index in range(len(any_list) - 1):
#         current_element = any_list[index]
#         next_element = any_list[index + 1]
#
#         if len(current_element) > len(next_element):
#             any_list[index], any_list[index + 1] = next_element, current_element  # Изменить элемент списка можно только по индексу этого элемента.
#                                                                                   # (Тема изменяемых и неизменяемых типов данных пройдем позже
#
#         elif len(current_element) == len(next_element) and current_element > next_element:  # При сравнении строк в python, они сравниваются по алфавиту
#             any_list[index], any_list[index + 1] = next_element, current_element
#
# print(any_list)



# Дан список состоящий из строк и чисел. Необходимо отсортировать список в порядке возрастания, учитывая то что строки сортируются по их длине.
# Пример:
# any_list = [1, 2, 'Hello', 'Tom', 7]
# Вывод: [1, 2, Tom, Hello, 7]

# any_list = [1, 2, 'Hello', 'Tom', 7]
#
# for _ in range(len(any_list)):
#     for index in range(len(any_list) - 1):
#         current_element = any_list[index]  # Исходный элемент
#         next_element = any_list[index + 1]  # Исходный элемент
#
#         if isinstance(current_element, int):
#             current_element_value = current_element  # Приведенный формат
#         else:
#             current_element_value = len(current_element)  # Приведенный формат
#
#         if isinstance(next_element, int):
#             next_element_value = next_element  # Приведенный формат
#         else:
#             next_element_value = len(next_element)  # Приведенный формат
#
#         if current_element_value > next_element_value:
#             any_list[index], any_list[index + 1] = next_element, current_element  # При приведении элементов списка разных типов
#                                                                                   # к одному формату важно не изменять исходные элементы ( current_element и next_element)
#
# print(any_list)







#Дан спеисок чисел, необходимо отсортировать в порядке убывания, учитывая что числа сортируются по их длине.

#3543634
#9999999   - одинаковые числа

# any_list = [3543634, 436234523453245, 123, 345436, 9999999, 353246431, 12436, 450608]
#
# for _ in range(len(any_list)):
#
#     for index in range(len(any_list) - 1):
#         current_element = any_list[index]
#         next_element = any_list[index + 1]
#
#         if len(str(current_element)) < len(str(next_element)):
#             any_list[index], any_list[index + 1] = next_element, current_element
#
# print(any_list)


