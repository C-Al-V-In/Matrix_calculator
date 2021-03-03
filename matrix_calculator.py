import copy

choice = ''
rows = ''
columns = ''


# TODO improve the problem of print
def start():
    while True:
        print('1. Add matrices', '2. Multiply matrix by a constant', '3. Multiply matrices', '4. Transpose matrix',
              '5. Calculate a determinant', '6. Inverse matrix', '0. Exit', sep="\n")
        global choice
        choice = input()
        if choice == '1':
            print('Enter size of first matrix:')
            size()
            print('Enter first matrix:')
            matrix1 = formation()
            print('Enter size of second matrix:')
            size()
            print('Enter second matrix:')
            matrix2 = formation()
            print('The result is:')
            sum_up(matrix1, matrix2)
        elif choice == '2':
            print('Enter size of matrix:')
            size()
            print('Enter matrix:')
            matrix = formation()
            print('Enter constant:')
            multiple = input()
            multiply(matrix, multiple)
        elif choice == '3':
            print('Enter size of first matrix:')
            size()
            print('Enter first matrix:')
            matrix1 = formation()
            print('Enter size of second matrix:')
            size()
            print('Enter second matrix:')
            matrix2 = formation()
            print('The result is:')
            matrix_multiply(matrix1, matrix2)
        elif choice == '4':
            transpose()
        elif choice == '5':
            print('Enter matrix size:')
            size()
            print('Enter matrix:')
            matrix = formation()
            print('The result is:')
            print(calculate_determinant(matrix))
            print()
        elif choice == '6':
            print('Enter matrix size:')
            size()
            print('Enter matrix:')
            matrix = formation()
            inverse(matrix)
        elif choice == '0':
            exit()


def size():
    global rows, columns
    rows, columns = input().split()


def formation():
    matrix = []
    for i in range(int(rows)):
        data = input()
        if len(data.split()) == int(columns):
            matrix.append([float(j) for j in data.split()])
        else:
            print('The operation cannot be performed.')
            print()
            start()
    return matrix


def sum_up(matrix1: list, matrix2: list):
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            print(matrix1[i][j] + matrix2[i][j], end=' ')
        print()
    print()


def multiply(matrix: list, multiple: str):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j] * float(multiple), end=' ')
        print()
    print()


def matrix_multiply(matrix1: list, matrix2: list):
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            print(sum([matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2))]), end=' ')
        print()
    print()


def transpose():
    print('1. Main diagonal', '2. Side diagonal', '3. Vertical line', '4. Horizontal line', 'Your choice:', sep='\n')
    task = input()
    print('Enter matrix size:')
    size()
    print('Enter matrix:')
    matrix = formation()
    if task == '1':
        main_diagonal_transpose(matrix)
    elif task == '2':
        side_diagonal_transpose(matrix)
    elif task == '3':
        vertical_line_transpose(matrix)
    elif task == '4':
        horizontal_line_transpose(matrix)


def main_diagonal_transpose(matrix):
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            print(matrix[j][i], end=' ')
        print()
    print()


def side_diagonal_transpose(matrix):
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            print(matrix[-1 - j][-1 - i], end=' ')
        print()
    print()


def vertical_line_transpose(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][-1 - j], end=' ')
        print()
    print()


def horizontal_line_transpose(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[-1 - i][j], end=' ')
        print()
    print()


def minor_creator(x, y, matrix):
    minors = copy.deepcopy(matrix)
    del minors[x]
    for i in range(len(minors)):
        del minors[i][y]
    return minors


def cofactor_creator(matrix):
    cofactors = []
    for i in range(len(matrix)):
        cofactors.append([])
        for j in range(len(matrix[0])):
            cofactors[i].append(calculate_determinant(minor_creator(i, j, matrix)) * ((-1) ** (i + j)))
    return cofactors


def calculate_determinant(matrix):
    result = 0
    if len(matrix) == len(matrix[0]) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    elif len(matrix) == len(matrix[0]) == 1:
        return matrix[0][0]
    else:
        for i in range(len(matrix[0])):
            minor = minor_creator(0, i, matrix)  # 以第一行展开
            result += matrix[0][i] * calculate_determinant(minor) * ((-1) ** i)
        return result


def inverse(matrix):
    if not calculate_determinant(matrix) or len(matrix) == 1:
        print("This matrix doesn't have an inverse.")
        print()
    else:
        adjugate = []
        cofactors = cofactor_creator(matrix)  # 有待优化
        for i in range(len(cofactors[0])):
            adjugate.append([])
            for j in range(len(cofactors)):
                adjugate[i].append(cofactors[j][i])
        multiply(adjugate, 1 / calculate_determinant(matrix))


if __name__ == '__main__':
    start()
