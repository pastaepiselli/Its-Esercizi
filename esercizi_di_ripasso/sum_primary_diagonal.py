def sum_primary_diagonal(matrix: list[list]) -> int:
    sum: int = 0
    i = 0
    for elem in matrix:
        sum += elem[i]
        i += 1

    return sum

mat1 = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

print(sum_primary_diagonal(mat1))


def sum_secondary_diagonal(matrix: list[list]) -> int:

    sum: int = 0 
    i = 2
    for elem in matrix:
        sum += elem[i]
        i -= 1

    return sum

print(sum_secondary_diagonal(mat1))