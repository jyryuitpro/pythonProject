def factorial(num):
    if num > 1:
        return num * factorial(num - 1)
    else:
        return num

for num in range(10):
    print(factorial(num))