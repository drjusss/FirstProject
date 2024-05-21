
# memorized_password = 'Password'
# password_is_valid = False
# trying = 0
#
# while not password_is_valid and trying < 3:
#     trying += 1
#     password = input('Введите пароль: ')
#     password_is_valid = password == memorized_password
#     if password_is_valid is False and trying != 3:
#         print('Пароль неверный попробуйте ещё раз.')
#
# if password_is_valid:
#     print('Вы успешно авторизованы!')
# else:
#     print('Количество попыток исчерпано, профиль заблокирован')
#
# number = 0
# number_count = 0
#
# while number_count != 10:
#     number_count += 1
#     number = 0
#     while number != 10:
#         number += 1
#         print('1', end=" ")
#     print()

# list_object = ['Hello', 2, 3, 'World123', 5]
#
# for current_element in list_object:
#     print(current_element)
#
# for current_index in range(len(list_object)):
#     print('current_index: ' + str(current_index))
#     print('current_element: ' + str(list_object[current_index]))
#     print()

# range_values = range(11)
# print(list(range_values))