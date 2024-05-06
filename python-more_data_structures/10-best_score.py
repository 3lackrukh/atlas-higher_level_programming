#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary or not any(a_dictionary.values()):
        return None
    high_score = next(val for val in a_dictionary.values() if val is not None)
    for key, val in a_dictionary.items():
        if val is None:
            continue
        if val >= high_score:
            high_score = val
            champ = key
    return champ
