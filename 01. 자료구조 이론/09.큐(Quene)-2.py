import queue

data_queue = queue.LifoQueue()

data_queue.put("funcoding")
data_queue.put(1)

# print(data_queue.qsize())
# print(data_queue.get())

data_queue = queue.PriorityQueue()

data_queue.put((10, "korea"))
data_queue.put((5, 1))
data_queue.put((15, "china"))

# print(data_queue.qsize())
# print(data_queue.get())

queue_list = list()

def enqueue(data):
    queue_list.append(data)

def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data

for index in range(10):
    enqueue(index)

print(len(queue_list))
print(queue_list)
print(dequeue())