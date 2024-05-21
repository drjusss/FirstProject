# current_list = [1, 2, 3]
# current_list.append([1, 2, 3])
# current_list.extend([1, 2, 3])
#
# print(current_list)

# string_object = 'Hello world!'
# new_string_object = string_object.replace('world', 'Самат')
#
# print(new_string_object)
# print(string_object)

# current_list.pop(3)
# print(current_list)

# current_list.reverse()
# print(current_list)
# print(current_list[2])
# print(current_list[3][0])
# print(current_list[-1])

# Дан список следующего формата: [1, 2, 3, [4, 5, 6], 7, 8, 9, [10, 11, 12]], нужно его перевести в список:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# current_list = [
#     1, 2, 3,
#     [4, 5, 6],
#     7, 8, 9,
#     [10, 11, 12]
# ]
# result = []
#
# for element in current_list:
#     if isinstance(element, list):
#         result.extend(element)
#     else:
#         result.append(element)
#
# print(result)

# current_list = [
#     1, 2, 3,
#     [
#         4, 5, 6,
#         [7, 8, 9],
#         10, 11, 12,
#     ],
#     13, 14, 15
# ]
#
# result = []
#
# for element in current_list:
#     if isinstance(element, list):
#         for sub_element in element:
#             if isinstance(sub_element, list):
#                 result.extend(sub_element)
#             else:
#                 result.append(sub_element)
#     else:
#         result.append(element)
#
# print(result)

# current_tuple = (1, 2, 3, 2, 3, 1, 2)

# print(current_tuple.index(2, 4))
# print(current_tuple.count(3))

# a, b, c, d = (1, 2, 3, 4)
#
# print(a)
# print(b)
# print(c)

# a = 1, 2, 3
#
# print(a)

current_set = {(1, 2, 3), '1', 2, 2, 3}
# new_current_set = current_set.copy()
# new_current_set.add(5)
#
# print(new_current_set)
# print(current_set)

current_set_2 = {1, 2, 3, 4, 5}
# result_current_set = current_set.union(current_set_2)
# result_current_set_2 = current_set | current_set_2
# result_current_set = current_set.intersection(current_set_2)
# result_current_set_2 = current_set & current_set_2
# result_current_set = current_set.difference(current_set_2)
# result_current_set_2 = current_set_2 - current_set
current_set.difference_update(current_set_2)

print(current_set)
print(current_set_2)
# print(result_current_set)
# print(result_current_set_2)

