for X in range(1, 101):
    if X % 3 == 0 and X % 5 == 0:
        print("FizzBuzz")
    elif X % 3 == 0:
        print("Fizz")
    elif X % 5 == 0:
        print("Buzz")
    else:
        print(X)