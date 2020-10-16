hash_table = list([0 for i in range(8)])

# 해쉬 키 생성
def get_key(data):
    return hash(data)

# 해쉬 함수
def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] = value
                return
        hash_table[hash_address].append([index_key, value])
    else:
        hash_table[hash_address] = [[index_key, value]]

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None

print (hash('Dave') % 8)
print (hash('Dd') % 8)
print (hash('Data') % 8)

save_data('Dd', '1201023010')
save_data('Data', '3301023010')
read_data('Dd')

print(hash_table)