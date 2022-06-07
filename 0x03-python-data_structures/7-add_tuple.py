#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = []
    if len(tuple_b) == 0:
        for i in range(len(tuple_a)):
            new_tuple.append(tuple_a[i])
    elif len(tuple_a) == 0:
        for j in range(len(tuple_b)):
            new_tuple.append(tuple_b[j])
    elif len(tuple_a) >= 2 and len(tuple_b) >= 2:
        for k in range(2):
            new_tuple.append(tuple_a[k] + tuple_b[k])
    elif len(tuple_a) < 2 and len(tuple_b) >= 2:
        new_tuple.append(tuple_a[0] + tuple_b[0])
        new_tuple.append(0 + tuple_b[1])
    elif len(tuple_a) >= 2 and len(tuple_b) < 2:
        new_tuple.append(tuple_a[0] + tuple_b[0])
        new_tuple.append(tuple_a[1] + 0)
    return tuple(new_tuple)
