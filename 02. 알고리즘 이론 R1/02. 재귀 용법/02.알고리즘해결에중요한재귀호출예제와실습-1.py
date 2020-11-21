import random

def multiple(num):
    if num <= 1:
        return num
    return num * multiple(num - 1)

def sum_list(data):
    if len(data) <= 1:
        return data[0]
    return data[0] + sum_list(data[1:])

data = random.sample(range(100), 10)
print(sum_list(data))

def palindrome(string):
    if len(string) <= 1:
        return True

    if string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return False
