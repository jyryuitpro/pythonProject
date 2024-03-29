import random

def bubblesort(data):
    for index in range(len(data) - 1):
        swap = False
        for index2 in range(len(data) - index - 1):
            if data[index2] > data[index2 + 1]:
                data[index2], data[index2 + 1] = data[index2 + 1], data[index2]
                swap = True

        if swap == False:
            break
    return data

data_list = random.sample(range(100), 50)
print(data_list)
print(bubblesort(data_list))

# 알고리즘 분석
# O(n^2)
# O(n)