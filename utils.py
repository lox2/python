def matrix_print(matrix: list) -> None:
    for line in matrix:
        print(line)


def refactor(field):
    matrix = [[] for i in range(len(field))]
    for i in range(len(field)):
        for j in range(len(field[i])):
            matrix[i].append(field[i][j].char())
    return matrix