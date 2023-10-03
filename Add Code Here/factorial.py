
# Defining the function which accepts only one number
def factorial(num):
    return 1 if num in [0, 1] else num * factorial(num - 1)


print(factorial(5)) # finally we print the answer with a parameter, you can get user defined input as well.
