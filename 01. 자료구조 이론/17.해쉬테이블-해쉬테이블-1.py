hash_table = list(0 for i in range(10))
print(hash_table)

def hash_func(key):
    return key % 5

data1 = "Andy"
data2 = "Dave"
data3 = "Trump"

# ord(): 문자의 ASCII(아스키)코드 리턴
print(ord(data1[0]), ord(data2[0]), ord(data3[0]))  # key
print(hash_func(ord(data1[0])), hash_func(ord(data2[0])), hash_func(ord(data3[0]))) # hash

def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value

storage_data("Andy", "01055553333")
storage_data("Dave", "010FFFF3333")
storage_data("Trump", "01022223333")

def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]

print(get_data("Andy"))