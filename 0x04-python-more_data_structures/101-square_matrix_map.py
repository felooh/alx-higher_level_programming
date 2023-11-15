#!/usr/bin/python3
<<<<<<< HEAD
def square_matrix_map(matrix=[]):
    return (list(map(lambda x: list(map(lambda y: y**2, x)), matrix)))


=======

def square_matrix_map(matrix=[]):
    """computes the square value of all integers """
    return (list(map(lambda x: list(map(lambda y: y ** 2, x[:])), matrix)))
>>>>>>> 353ce5250633ccf4050ae25a3333be2157cf0033
