#!/usr/bin/python3
import sys


if __name__ == "__main__":
    """Main module"""

    if len(sys.argv) == 2:
        if not isinstance(int(sys.argv[1]), int):
            print("N must be a number")
            exit(1)
        elif int(sys.argv[1]) < 4:
            print("N must be at least 4")
            exit(1)
        else:
            print("DO THIS")
    else:
        print("Usage: nqueens N")
        exit(1)
