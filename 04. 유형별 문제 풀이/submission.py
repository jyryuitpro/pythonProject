queue = list(map(int, input().split(' ')))
print(queue) # [1, 2, 3, 4] 문서의 중요도

for idx, i in enumerate(queue):
    print(idx, i)

# 0 1
# 1 2
# 2 3
# 3 4

queue = [(i, idx) for idx, i in enumerate(queue)]

print(queue) # [(1, 0), (2, 1), (3, 2), (4, 3)]

print(max(queue, key=lambda x: x[0]))