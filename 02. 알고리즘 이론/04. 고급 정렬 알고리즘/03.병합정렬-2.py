def split(data):
    medium = int(len(data) / 2)
    left = data[:medium]
    right = data[medium:]
    print(left, right)

# data_list = [3, 4, 1, 3, 2]
# split(data_list)

def mergesplit(data):
    if len(data) <= 1:
        return data

    medium = int(len(data) / 2)
    left = mergesplit(data[:medium])
    right = mergesplit(data[medium:])

    # print(left, right, end=' ')

    return merge(left, right)

data_list = [3, 4, 1, 3]
mergesplit(data_list)

    # return merge(left, right)