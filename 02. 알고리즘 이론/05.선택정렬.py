import random

def selection_sort(data_list):
    for stand_index in range(len(data_list) - 1):
        # lowest_index = stand_index
        for check_index in range(stand_index + 1, len(data_list)):
            if data_list[stand_index] > data_list[check_index]:
                # lowest_index = check_index
                data_list[stand_index], data_list[check_index] = data_list[check_index], data_list[stand_index]
    return data_list

data_list = random.sample(range(100), 4)
print(selection_sort(data_list))