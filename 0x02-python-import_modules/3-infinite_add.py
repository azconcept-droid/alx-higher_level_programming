#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    if length == 1:
        print("0")
    else:
        i = 1
        sum = 0
        while i < length:
            sum += int(sys.argv[i])
            i += 1
        print("{:d}".format(sum))
