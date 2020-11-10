hash_table = list([0 for i in range(8)])

# 해쉬 키 생성
def get_key(data):
    return hash(data)

# 해쉬 함수
def hash_function(key):
    return key % 8

def save_data(data, value):
    hash_address = hash_function(get_key(data))
    hash_table[hash_address] = value

def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]

save_data('Dave', '01020302000')
save_data('Andy', '01033232200')

print(hash_table)
print()
print(read_data('Dave'))


