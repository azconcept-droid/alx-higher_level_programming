#!/usr/bin/python3
def multiple_returns(sentence):
    new_tuple = []
    new_tuple.append(len(sentence))
    if sentence == "":
        new_tuple.append("None")
    else:
        new_tuple.append(sentence[0])
    return tuple(new_tuple)
