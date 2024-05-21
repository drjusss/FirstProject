# Вывести матрицу 5х5 состоящую из матриц 10х10 следующего вида:
# 0123456789
# ...
# 0123456789; изменять начало цикла и 2 вложенный

amount_matrix_raw = int(input('Введите количество матриц в строчку: '))
amount_matrix_col = int(input('Введите количество матриц в столбец: '))
amount_raw = int(input('Введите количество строк в матрице: '))
amount_col = int(input('Введите количество столбцов в матрице: '))

for matrix_raw in range(amount_matrix_raw):
    for raw in range(amount_raw):
        for matrix_col in range(amount_matrix_col):
            for col in range(amount_col):
                print(col, end=" ")
            print(end=" ")
        print()
    print()
