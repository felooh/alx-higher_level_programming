#!/usr/bin/python3
<<<<<<< HEAD
def search_replace(my_list, search, replace):
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return (new_list)

=======

def search_replace(my_list, search, replace):
    """Replace all occurrences of an element by another in a new list."""
    new_list = my_list[:]
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return (new_list)
>>>>>>> 353ce5250633ccf4050ae25a3333be2157cf0033
