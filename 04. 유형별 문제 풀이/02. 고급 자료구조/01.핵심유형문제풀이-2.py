# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 5             : 첫째 줄에 자연수 N(1≤N≤100,000)이 주어진다.
# 4 1 5 2 3     : 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
# 5             : 다음 줄에는 M(1≤M≤100,000)이 주어진다.
# 1 3 7 9 5     : 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다.

n_count = int(input())
n_list = list(map(int, input().split()))

m_count = int(input())
m_list = list(map(int, input().split()))

match_flag = 0
match_list = []

for m in range(m_count):
    for n in range(n_count):
        if m_list[m] == n_list[n]:
            match_flag += 1

    if match_flag > 0:
        match_list.append(1)
    else:
        match_list.append(0)

    match_flag = 0

print(match_list)






