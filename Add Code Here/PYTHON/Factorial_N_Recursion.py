def factorial(number):
    return 1 if number == 0 else number * factorial(number - 1)


N = int(input("Enter N: "))
result = factorial(N)
print(f"The factorial of {N} is {result}")
