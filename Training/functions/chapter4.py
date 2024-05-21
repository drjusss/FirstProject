#                                       Упражнение 85. Вычисляем длину гипотенузы
# (23 строки)
# Напишите функцию, принимающую на вход длины двух катетов прямоугольного треугольника и
# возвращающую длину гипотенузы, рассчитанную по теореме Пифагора. В главной программе должен осуществляться
# запрос длин сторон у  пользователя, вызов функции и  вывод на экран
# полученного результата.

# # import math  - импорт библиотеки
# from math import sqrt  # - импорт библиотеки
#
#
# def calculate_hypotenuse(leg1, leg2):
#     # hypotenuse = math.sqrt(leg1 * leg1 + leg2 * leg2)
#     hypotenuse = sqrt(leg1 ** 2 + leg2 ** 2)
#     return hypotenuse
#
#
# def main():
#     leg1 = int(input('Введите длину первого катета: '))
#     leg2 = int(input('Введите длину второго катета: '))
#     hypotenuse = calculate_hypotenuse(leg1, leg2)
#     print(f' Гипотенуза с катетами: {leg1} и {leg2} равна {hypotenuse}')
#
#
# main()


#                                               Упражнение 86. Плата за такси
# (22 строки)
# Представьте, что сумма за пользование услугами такси складывается из
# базового тарифа в  размере $4,00 плюс $0,25 за каждые 140 м поездки.
# Напишите функцию, принимающую в качестве единственного параметра
# расстояние поездки в километрах и возвращающую итоговую сумму оплаты такси. В  основной программе должен демонстрироваться результат
# вызова функции.
#
# def calculate_price(distance):
#     basic_tariff = 4.00
#     price_per_140 = 0.25
#     total_price_140 = distance // 140 * price_per_140
#     total_sum = basic_tariff + total_price_140
#     return total_sum
#
#
# def main():
#     distance = int(input('Введите длину поездки: '))
#     total_sum = calculate_price(distance)
#     print(total_sum)
#
#
# main()


#                                           Упражнение 87. Расчет стоимости доставки
# (23 строки)
# Интернет-магазин предоставляет услугу экспресс-доставки для части
# своих товаров по цене $10,95 за первый товар в заказе и $2,95 – за все
# последующие. Напишите функцию, принимающую в качестве единственного параметра количество товаров в  заказе и  возвращающую общую
# сумму доставки. В  основной программе должны производиться запрос
# количества позиций в  заказе у  пользователя и  отображаться на экране
# сумма доставки.


# def calculation_total_delivery_amount(product):
#     cost_of_1_product = 10.95
#     cost_per_product = 2.95
#     cost_of_delivery = cost_of_1_product + (cost_per_product * (product - 1))
#     return cost_of_delivery
#
#
# def main():
#     product = int(input('Введите количество товаров: '))
#     result = calculation_total_delivery_amount(product)
#     print(result)
#
#
# main()


#                                       Упражнение 88. Медиана трех значений
# (Решено. 43 строки)
# Напишите функцию, которая будет принимать на вход три числа в качестве параметров и возвращать их медиану. В основной программе должен
# производиться запрос к пользователю на предмет ввода трех чисел, а также вызов функции и отображение результата.


# def find_median(number1, number2, number3):
#
#     list_of_numbers = [number1, number2, number3]
#     list_of_numbers.sort()
#     median = list_of_numbers[1]
#     return median
#
#
# def main():
#     number1 = int(input('Введите первое число: '))
#     number2 = int(input('Введите второе число: '))
#     number3 = int(input('Введите третье число: '))
#     median = find_median(number1, number2, number3)
#     print(f'Медиана указанных числе равна: {median}')
#
#
# main()


#                                       Упражнение 89. Переводим целые числа в числительные
# (47 строк)
# Такие слова, как первый, второй, третий, являются числительными. В данном упражнении вам необходимо написать функцию, принимающую на
# вход в качестве единственного аргумента целое число и возвращающую
# строковое значение, содержащее соответствующее числительное (на английском языке). Ваша функция должна обрабатывать числа в диапазоне
# от 1 до 12. Если входящее значение выходит за границы этого диапазона,
# вывод должен оставаться пустым. В основной программе запустите цикл
# по натуральным числам от 1 до 12 и выведите на экран соответствующие
# им числительные. Ваша программа должна запускаться только в том случае, если она не импортирована в виде модуля в другой файл.


# def conversion_to_numerals(number):  # Надо доработать, потому что выводиться весь список, а мне нужно только 1 значение
#
#     dict_of_numerals = {
#         1: 'one',
#         2: 'two',
#         3: 'three',
#         4: 'four',
#         5: 'five',
#         6: 'six',
#         7: 'seven',
#         8: 'eight',
#         9: 'nine',
#         10: 'ten',
#         11: 'eleven',
#         12: 'twelve',
#     }
#
#     if number in dict_of_numerals:
#         number = dict_of_numerals[number]
#         return number
#
#
# def main():
#     number = int(input('Ввелите число: '))
#     number_string = conversion_to_numerals(number)
#     if number_string:
#         print(number_string)
#
#
# main()


#                                   Упражнение 91. Григорианский календарь в порядковый
# (72 строки)
# Порядковая дата содержит номер года и порядковый номер дня в этом
# году – оба в целочисленном формате. При этом год может быть любым
# согласно григорианскому календарю, а номер дня – числом в интервале
# от 1 до 366 (чтобы учесть високосные годы). Порядковые даты удобно
# использовать при расчете разницы в  днях, когда счет ведется именно
# в днях, а не месяцах. Например, это может касаться 90-дневного периода
# возврата товара для покупателей, расчета срока годности товаров или
# прогнозируемой даты появления малыша на свет.
# Напишите функцию с именем ordinalDate, принимающую на вход три
# целых числа: день, месяц и год. Функция должна возвращать порядковый
# номер заданного дня в указанном году. В основной программе у пользователя должны запрашиваться день,
# месяц и год соответственно и выводиться на экран порядковый номер дня в заданном году. Программа должна
# запускаться только в том случае, если она не импортирована в виде модуля в другой файл.


# def get_february_ordinal_day(month_index: int, year: int) -> int:
#
#     if year % 4 == 0:
#         return 29
#     return 28
#
#
# def get_ordinal_day(year: int, month: int, day: int) -> int:
#     amount_days = 0
#     for month_index in range(1, month):
#         if month_index <= 7 and month_index % 2 == 0:
#             if month_index == 2:
#                 amount_days += get_february_ordinal_day(month_index=month_index, year=year)
#             else:
#                 amount_days += 30
#         elif month_index <= 7 and month_index % 2 != 0:
#             amount_days += 31
#         elif month_index > 7 and month_index % 2 == 0:
#             amount_days += 31
#         elif month_index > 7 and month_index % 2 != 0:
#             amount_days += 30
#     amount_days += day
#     return amount_days
#
#
# def main() -> None:
#     print(get_ordinal_day(year=2023, month=6, day=2))
#
#
# if __name__ == '__main__':
#     main()


#                                                   Упражнение 93. Центрируем строку
# (Решено. 29 строк)
# Напишите функцию, которая будет принимать в  качестве параметров
# строку s, а также ширину окна в символах – w. Возвращать функция должна новую строку, в которой в начале добавлено необходимое количество
# пробелов, чтобы первоначальная строка оказалась размещена по центру заданного окна. Новая строка должна формироваться по следующему
# принципу:
#  если длина исходной строки s больше или равна ширине заданного
# окна, возвращаем ее в неизменном виде;
#  в противном случае должна быть возвращена строка s с ведущими
# пробелами в количестве (len(s) – w) // 2 штук.
# В вашей основной программе должен осуществляться пример вывода
# нескольких строк в окнах разной ширины.


def center_the_line(any_string: str, length_window: int) -> str:

    if len(any_string) >= length_window:
        return any_string
    else:
        space_counter = (length_window - len(any_string)) // 2
        return " " * space_counter + any_string


def main():
    result = center_the_line(any_string='Window', length_window=50)
    print(result)


if __name__ == '__main__':
    main()