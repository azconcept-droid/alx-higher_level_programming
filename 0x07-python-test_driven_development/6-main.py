#!/usr/bin/python3
max_integer = __import__('6-max_integer').max_integer

print(max_integer([1, 2, 3, 4]))
print(max_integer([1, 3, 4, 2]))
print(max_integer([]))
print(max_integer([10]))
print(max_integer([-10, -2, -1, -3]))
# print(max_integer([-10, 'c', 90, 'python']))
print(max_integer((3, 9, 7, 89)))
# print(max_integer([0, (0, )]))
print(max_integer(['Python', 'is', 'fun']))
print(max_integer('Cisfun'))
# print(max_integer(50))
print(max_integer(''))
print(max_integer([
            3245, 323232, 2132323, 3233, 221,
            21323, 32323, 3323, 54545, 323, 23,
            3233, 7566, 43434, 42434, 45, 324, 3]))
print(max_integer([
            float("inf"), 8903283926, 89892382683283
            ]))
print(max_integer([
            float("-inf"), 0, -1
            ]))