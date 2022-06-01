#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
n = number
if n < 0:
    l = (-1 * number) % 10
    if l == 0:
        print('Last digit of {:d} is {:d} and is 0'.format(n, l))
    elif l < 6 and l != 0:
        print('Last digit of {: d} is -{} and is less than 6 and not 0'.format(n, l))
elif n > 0:
    l = n % 10
    if l == 0:
        print('Last digit of {:d} is {:d} and is 0'.format(n, l))
    elif l > 5:
        print('Last digit of {:d} is {} and is greater than 5'.format(n, l))
    elif l < 6 and l != 0:
        print('Last digit of {:d} is {} and is less than 6 and not 0'.format(n, l))
elif n == 0:
    l = 0
    print('Last digit of {:d} is {} and is 0'.format(n, l))
