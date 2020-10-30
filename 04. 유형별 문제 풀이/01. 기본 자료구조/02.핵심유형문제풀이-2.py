# 1. 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
# 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
# A B C D
# 2 1 4 3
# 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다.

# 예제 출력 1
# 3             : test case의 수

# 1 0           : 문서의 수 N(100이하) | 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue의 어떤 위치에 있는지를 알려주는 M(0이상 N미만)
# 5             : N개 문서의 중요도가 주어지는데, 중요도는 1 이상 9 이하 | 중요도가 같은 문서가 여러 개 있을 수도 있다.

# 4 2           : 문서의 수 N(100이하) | 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue의 어떤 위치에 있는지를 알려주는 M(0이상 N미만)
# 1 2 3 4       : N개 문서의 중요도가 주어지는데, 중요도는 1 이상 9 이하 | 중요도가 같은 문서가 여러 개 있을 수도 있다.

# 6 0           : 문서의 수 N(100이하) | 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue의 어떤 위치에 있는지를 알려주는 M(0이상 N미만)
# 1 1 9 1 1 1   : N개 문서의 중요도가 주어지는데, 중요도는 1 이상 9 이하 | 중요도가 같은 문서가 여러 개 있을 수도 있다.

# 예제 출력 1
# 1
# 2
# 5

test_case = int(input())

for _ in range(test_case):
    n, m = list(map(int, input().split(' ')))
    queue = list(map(int, input().split(' ')))
    queue = [(i, idx) for idx, i in enumerate(queue)]   # [(2, 0), (1, 1), (4, 2), (3, 3)]

    count = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            if queue[0][1] == m:
                print(count)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))


