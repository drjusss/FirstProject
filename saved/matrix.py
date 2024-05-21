height_nested_matrix = int(input('Введите число высоты вложенной матрицы: '))  # ВЫСОТА ВЛОЖЕННОЙ МАТРИЦЫ
length_nested_matrix = int(input('Введите число длины вложенной матрицы: '))   # ДЛИНА ВЛОЖЕННОЙ МАТРИЦЫ
length_result_matrix = int(input('Введите число ширины итоговой матрицы: '))   # ширина финальной матрицы
height_result_matrix = int(input('Введите число высоты итоговой матрицы: '))  # высота финальной матрицы

# matrix = list()
# matrix_row = list()

# deep_matrix = [
#     [
#         ['x' for length_index in range(length)]
#         for height_index in range(height)
#     ]
#     if deep_index % 2 == 0 else
#     [
#         ['0' for length_index in range(length)]
#         for height_index in range(height)
#     ]
#     for deep_index in range(deep)
# ]

# for deep_index in range(deep):
#     for matrix in deep_matrix:
#         print(matrix[deep_index], end='    ')
#     print()


def create_o_matrix() -> list:

    matrix = [
        ['0' for _ in range(length_nested_matrix)]
        for _ in range(height_nested_matrix)
    ]
    return matrix


def create_x_matrix() -> list:
    matrix = [
        ['x' for _ in range(length_nested_matrix)]
        for _ in range(height_nested_matrix)
    ]
    return matrix


def create_result_matrix_row() -> list:
    result_matrix_row = list()

    for width_index in range(length_result_matrix):
        if width_index % 2 == 0:
            current_matrix = create_o_matrix()
        else:
            current_matrix = create_x_matrix()

        result_matrix_row.append(current_matrix)
    return result_matrix_row


def main():
    result_matrix = list()
    for _ in range(height_result_matrix):
        result_matrix_row = create_result_matrix_row()
        result_matrix.append(result_matrix_row)

    for height_index in range(height_result_matrix):
        for nested_height_index in range(height_nested_matrix):
            for length_index in range(length_result_matrix):
                print(result_matrix[height_index][length_index][nested_height_index], end='    ')
            print()
        print()


if __name__ == '__main__':
    main()
# for height_index in range(height):
#     matrix_row = list()
#     for length_index in range(length):
#         matrix_row.append('x')
#     matrix.append(matrix_row)
# print(*matrix, sep='\n')

