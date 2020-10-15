import random

def bubblesort(data_list):
    for turn in range(len(data_list)-1):
        for check in range(len(data_list) - turn -1):
            if data_list[check] > data_list[check + 1]:
                data_list[check], data_list[check +1] = data_list[check +1], data_list[check]
    return data_list

data_list = random.sample(range(100), 50)
print(bubblesort(data_list))



