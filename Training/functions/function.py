#
# # def clear_text(input_string, symbol_list):
# #     result = str()
# #
# #     for symbol in input_string:
# #         if symbol.lower() not in symbol_list:
# #             result = f'{result}{symbol}'
# #
# #     print(result)
# #     return 2
# #
# #
# # def main():
# #     min_value = min([1, 2, 3])
# #     print(f'Функция "min" - возвращает {min_value}')
# #     result_clear_text = clear_text('ABCEDF', ['a', 'b', 'c'])
# #     print(f'Функция "clear_text" - возвращает {result_clear_text}')
# #
# #
# # main()
#
#
#
# # def get_most_number(number1, number2):
# #     if number1 > number2:
# #         return number1
# #     elif number1 < number2:
# #         return number2
# #     else:
# #         return number1
# #
# #
# # def main():
# #     number1 = int(input('Введите первое число: '))
# #     number2 = int(input('Введите второе число: '))
# #     get_most_number(number1, number2)
# #     result = get_most_number(number1, number2)
# #     print(result)
# #
# #
# # main()
# # * - распаковка коллекций
# # ** - распаковка словарей
#
#
# # variable = 1
# # print(type(variable))
# # variable: str = 'text'
# # print(type(variable))
# # variable = 1
# # print(type(variable))
#
#
# # def smth_function(name: list, surname: str) -> list:
# #     name.append(surname)
# #     return name
# #
# #
# # def main():
# #     result = smth_function(name=['text'], surname='5')
# #     print(result)
# #     name = 'Andrey'
# #
# # main()
#
#
# # ***ГЕНЕРАТОРЫ***
#
# # def generate_big_list():
# #     result = list()
# #     for number in range(10_000_000):
# #         result.append(number)
# #     return result
# #     # yield
# #
# #
# # def test_func(var: int) -> None:
# #     print(var)
# #
# #
# # def main() -> None:
# #     start_time = time.time()
# #     result = generate_big_list()
# #     print(result)
# #     for element in result:
# #         print(element, end=' ')
# #     stop_time = time.time()
# #     print(f'Функция выполнялась {stop_time - start_time} секунд.')
# #     test_func(1)
# #
# #
# # main()
# # ***Функция обертка***
#

# def wrap_to_stopwatch(function: typing.Callable, *args, **kwargs) -> typing.Any:  # Callable - вызываемый(функции), Any - что угодно.
#     start_time = time.time()
#     result = function(*args, **kwargs)
#     stop_time = time.time()
#     result_time = stop_time - start_time
#     print(f'Функция работала {result_time} секунд.')
#     return result

# ***ДЕКОРАТОРЫ*** (@)


# def stopwatch_wrapper(function: typing.Callable) -> typing.Callable:
#     def wrapper(*args, **kwargs) -> typing.Any:
#         start_time = time.time()
#         result = function(*args, **kwargs)
#         stop_time = time.time()
#         result_time = stop_time - start_time
#         print(f'Функция работала {result_time} секунд.')
#         return result
#     return wrapper
#
#
# @stopwatch_wrapper
# def test_function(amount) -> list:
#     result = list()
#     for number in range(1, amount):
#         result.append(number ** 10)
#     return result
#
#
# def main():
#     result = test_function(amount=10_000)
#     print(test_function.__name__)
#     # print(result)
#
#
#
# main()

# ***Рекурсия***

# some_list = list()
#
#
# def test_function(amount: int) -> None:
#     if amount > 0:
#         amount -= 1
#         test_function(amount)
#         some_list.append(amount)
#     print(amount)
#
#
# def main():
#     test_function(10)
#     print(some_list)

# main()
#
# ***Лямбда функции*** - функция "1 строчка"

def sum_2_numbers(number1: int, number2: int) -> int:
    return number1 + number2

lambda_sum_2_number = lambda num1, num2: num1 + num2

result1 = sum_2_numbers(number1=1, number2=2)
result2 = lambda_sum_2_number(num1=1, num2=2)

print(result1)
print(result2)


def print_cubes_of_numbers(number: int) -> None:
    if number == 0:
        return None
    print_cubes_of_numbers(number=number - 1)
    print(number ** 3, end=' ')


def print_numbers(amount: int) -> None:

    if amount > -1:
        amount -= 1
        print_numbers(amount)
        amount += 1
        print(amount)

@decorators.stopwatch
def main():
    number = int(input('Введите число: '))
    print_cubes_of_numbers(number=number)


if __name__ == '__main__':
    main()
    print_numbers(amount=10)

