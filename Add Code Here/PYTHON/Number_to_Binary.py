number=int(input())
temp=number
binary=""
while number>0:
    rem=number%2
    binary+=str(rem)
    number //= 2
print(f"The binary equivalent of {temp} is {binary[::-1]} .")
