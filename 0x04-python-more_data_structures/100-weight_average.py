#!/usr/bin/python3
<<<<<<< HEAD
def weight_average(my_list=[]):
    if not my_list:
        return 0

    num = 0
    den = 0

    for tup in my_list:
        num += tup[0] * tup[1]
        den += tup[1]

    return (num / den)

=======

def weight_average(my_list=[]):
    """Return the weighted average of all integers in a list of tuples."""
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    avg = 0
    size = 0
    for tup in my_list:
        avg += (tup[0] * tup[1])
        size += tup[1]
    return (avg / size)
>>>>>>> 353ce5250633ccf4050ae25a3333be2157cf0033
