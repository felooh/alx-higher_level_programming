#!/usr/bin/python3
<<<<<<< HEAD
def multiply_by_2(a_dictionary):
    new_dir = a_dictionary.copy()
    list_keys = list(new_dir.keys())

    for i in list_keys:
        new_dir[i] *= 2

    return (new_dir)

=======

def multiply_by_2(a_dictionary):
    """Return a new dictionary with all values multipled by 2."""
    return ({k: a_dictionary[k] * 2 for k in a_dictionary})
>>>>>>> 353ce5250633ccf4050ae25a3333be2157cf0033
