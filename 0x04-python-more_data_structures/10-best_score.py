#!/usr/bin/python3
<<<<<<< HEAD
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)

    return (max(a_dictionary, key=a_dictionary.get))

=======

def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    ret = list(a_dictionary.keys())[0]
    big = a_dictionary[ret]
    for k, v in a_dictionary.items():
        if v > big:
            big = v
            ret = k
    return (ret)
>>>>>>> 353ce5250633ccf4050ae25a3333be2157cf0033
