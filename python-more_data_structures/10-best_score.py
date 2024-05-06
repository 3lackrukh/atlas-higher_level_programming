#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary or not any(a_dictionary.values()):
        return None
    high_score = next(value for value in a_dictionary.values() if value is not None)
    for key, value in a_dictionary.items():
        if value is None:
            continue
        if value >= high_score:
            high_score = value
            champ = key
    return champ
