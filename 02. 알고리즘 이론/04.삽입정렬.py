import random

def insertion_sort(data_list):
    for turn in range(len(data_list) - 1):
        for check in range(turn + 1, 0, -1):
            if data_list[check] < data_list[check - 1]:
                data_list[check], data_list[check - 1] = data_list[check - 1], data_list[check]
            else:
                break
    return data_list

data_list = random.sample(range(100), 50)
print (insertion_sort(data_list))


for index in range(2, 0, -1):
    print(index)