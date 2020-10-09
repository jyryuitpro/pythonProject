data_stack = list()

data_stack.append(1)
data_stack.append(2)

# print(data_stack)
# print(data_stack.pop())

stack_list = list()

def push(data):
    stack_list.append(data)

def pop():
    data = stack_list[-1]
    del stack_list[-1]
    return data

for index in range(10):
    push(index)

print(pop())