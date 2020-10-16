import random

def qsort(data):
    if len(data) <= 1:
        return data

    left, right = list(), list()
    pivot = data[0]

    for index in range(1, len(data)):
        if pivot > data[index]:
            left.append(data[index])
        else:
            right.append(data[index])

    return qsort(left) + [pivot] + qsort(right)

def qsort_list_comprehension(data):
    if len(data) <= 1:
        return data

    pivot = data[0]

    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot <= item]

    return qsort(left) + [pivot] + qsort(right)

data_list = random.sample(range(100), 10)

print(data_list)
print(qsort(data_list))
print(qsort_list_comprehension(data_list))
