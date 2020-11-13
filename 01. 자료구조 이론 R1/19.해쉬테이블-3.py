#
hash_table = list([0 for i in range(8)])
# [0, 0, 0, 0, 0, 0, 0, 0]
print(hash_table)
hash_table[0] = list([11, '01012345678'])
print(hash_table)

# 해쉬 키 생성
def get_key(data):
    return hash(data)

# 해쉬 함수
def hash_function(key):
    return key % 8

def save_data(data, value):
    # 해쉬 키 생성 및 저장
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    # 현재 데이터가 들어가 있는 경우
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] == value
                return
        hash_table[hash_address].append([index_key, value])
    else:
        hash_table[hash_address] = list([index_key, value])

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(get_key(data))
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None