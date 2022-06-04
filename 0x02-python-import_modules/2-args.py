#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    if length == 1:
        print("0 arguments.")
    elif length == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(length - 1))
        i = 1
        while i < length:
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
