#!/usr/bin/python3
<<<<<<< HEAD
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for i in range(len(matrix)):
        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))

    return (new_matrix)

=======

def square_matrix_simple(matrix=[]):
    """Compute the square value of all integers of a matrix."""
    return ([list(map(lambda x: x * x, row)) for row in matrix])
>>>>>>> 353ce5250633ccf4050ae25a3333be2157cf0033
