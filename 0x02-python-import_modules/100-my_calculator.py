#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    length = len(sys.argv)
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print(exit(1))
    else:
        a = int(sys.argv[1])
        operator = sys.argv[2]
        b = int(sys.argv[3])
        if operator == "+":
            result = add(a, b)
            print("{:d} {} {:d} = {:d}".format(a, operator, b, result))
        elif operator == "-":
            result = sub(a, b)
            print("{:d} {} {:d} = {:d}".format(a, operator, b, result))
        elif operator == "*":
            result = mul(a, b)
            print("{:d} {} {:d} = {:d}".format(a, operator, b, result))
        elif operator == "/":
            result = div(a, b)
            print("{:d} {} {:d} = {:d}".format(a, operator, b, result))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            print(exit(1))
