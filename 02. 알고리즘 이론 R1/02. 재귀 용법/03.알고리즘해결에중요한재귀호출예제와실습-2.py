def func(n):
    print(n)
    if n == 1:
        return n

    if n % 2 == 1:
        return func((3 * n) + 1)
    else:
        return func(int(n / 2))

# func(3)

def func(data):
    if data == 1:
        return 1
    elif data == 2:
        return 2
    elif data == 3:
        return 4

    return func(data - 1) + func(data - 2) + func(data - 3)

print(func(4))