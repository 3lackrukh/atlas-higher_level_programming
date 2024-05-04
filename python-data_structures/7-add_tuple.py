#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    max_len = max(len(tuple_a), len(tuple_b))

    tuple_a = tuple_a + (0,) * (max_len - len(tuple_a))
    tuple_b = tuple_b + (0,) * (max_len - len(tuple_b))

    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return result
