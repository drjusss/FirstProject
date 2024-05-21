#
# dict_object = {
#     'Cashiers': {'Иванов Иван Иванович', 'Алексеев Алексей Алексеевич', 'Сергеев Сергей Сергеевич'},
#     'Security': 'Магомедов Магомед Магомедович',
#     'Directory': 'Алексеев Сергей Степанович',
#     'int': 2,
#     'float': 2.1
# }
#
# # print(dict_object['Cashiers'])
#
# dict_object['new key'] = ['new_value', 'new value 2']
#
# print(dict_object)
# dict_object['new key'] = 'new value 2'
# print(dict_object)

# Пользователь вводит какие-то значения до сих пор пока не введет 'END'. Эти значения должны сохраняться в словарь в следующем формате:
# {
# 'int': [...] - Все введённые данные, которые можно интерпретировать как 'int'
# ...
# 'str' [...] - Все введённые данные, которые можно интерпретировать как 'str'
# }
# int, str, bool, float, None,

# any_value = input('Введите значение: ')
# dict_result = {
#     'int': [],
#     'float': [],
#     'str': [],
#     'bool': [],
#     'NoneType': []
# }
#
# while any_value != 'END':
#
#     if any_value == 'None':
#         dict_result['NoneType'].append(any_value)
#         dict_result['NoneType'] = None
#
#     elif any_value == 'True':
#         dict_result['bool'].append(True)
#
#     elif any_value == 'False':
#         dict_result['bool'].append(False)
#
#     elif any_value.isdigit():
#         dict_result['int'].append(int(any_value))
#
#     elif any_value.count('.') == 1:
#         dot_index = any_value.index('.')
#         before_dot = any_value[:dot_index]
#         after_dot = any_value[dot_index + 1:]
#
#         if before_dot.isdigit() and after_dot.isdigit():
#             dict_result['float'].append(float(any_value))
#         else:
#             dict_result['str'].append(str(any_value))
#     else:
#         dict_result['str'].append(str(any_value))
#     any_value = input('Введите значение: ')
#
# print(dict_result)

dict_result = {
    'int': 1,
    'float': 1.1,
    'str': 'erdsfh',
    'bool': True,
    'NoneType': None
}

# dict_result.pop('int')
# print(dict_result)

# print(dict_result.keys())

print(dict_result.get('int', '123'))

# another_dict = dict_result.copy()

# dict_result.clear()
# print(dict_result)

# new_dict = dict.fromkeys([1, 2, 3, 4, 5], [])
# print(new_dict)

# new_dict2 = {key: 0 for key in [1, 2, 3, 4, 5]}
# print(new_dict2)

# print(dict_result.items())
# for key, value in dict_result.items():   #создание смписка из ключ=значение
#     print(f'{key}: {value}')

# dict_result.popitem()
# print(dict_result)

# dict_result.setdefault('int1', 123)
# print(dict_result)

# dict_result.update(dict_object)
# print(dict_result)

# print(dict_result.values())
