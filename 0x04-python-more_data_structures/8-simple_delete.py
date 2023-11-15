#!/usr/bin/python3
<<<<<<< HEAD
def simple_delete(a_dictionary, key=""):
    if a_dictionary.get(key) is not None:
        del a_dictionary[key]
    return (a_dictionary)

=======

def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return (a_dictionary)
>>>>>>> 353ce5250633ccf4050ae25a3333be2157cf0033
