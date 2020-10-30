queue = list(map(int, input().split(' ')))
queue = [(i, idx) for idx, i in enumerate(queue)]  # [(2, 0), (1, 1), (4, 2), (3, 3)]
print(queue)
print(queue[0][0])
print(queue[0][1])
print(max(queue, key=lambda x: x[0])[0])