def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            print(f"Fizz", end = " ")
        elseif i % 5 == 0:
            print(f"Buzz", end = " ")
        elseif i % 15 == 0:
            print(f"FizzBuzz", end = " ")
        else:
            print(f"{i:d}", end = " ")
