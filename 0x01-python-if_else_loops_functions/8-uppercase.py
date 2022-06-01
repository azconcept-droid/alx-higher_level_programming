def uppercase(str):
    for i in range(len(str)):
        num = ord(str[i])
        if num >= 65 and num <= 90:
            print('{}'.format(str[i]), end="")
