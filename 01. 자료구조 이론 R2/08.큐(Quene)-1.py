import queue

# 가장 일반적인 큐, FIFO(First-In, First-out)
data_queue = queue.Queue()

# Enqueue
data_queue.put("funcoding")
data_queue.put(1)
print(data_queue.qsize())

# Dequeue
print(data_queue.get())
print(data_queue.qsize())

# Dequeue
print(data_queue.get())
print(data_queue.qsize())
