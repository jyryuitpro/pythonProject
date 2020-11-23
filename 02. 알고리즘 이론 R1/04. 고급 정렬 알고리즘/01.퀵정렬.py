import random

def qsort_a(data):
    if len(data) <= 1:
        return data

    left, right = list(), list()
    pivot = data[0]

    for index in range(1, len(data)):
        if pivot > data[index]:
            left.append(data[index])
        else:
            right.append(data[index])

    return qsort_a(left) + [pivot] + qsort_a(right)

data_list = random.sample(range(100), 10)

print(data_list)
print(qsort_a(data_list))

def qsort_b(data):
    if len(data) <= 1:
        return data

    pivot = data[0]

    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot <= item]

    return qsort_b(left) + [pivot] + qsort_b(right)

print(data_list)
print(qsort_b(data_list))

