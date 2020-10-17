# https://www.acmicpc.net/problem/2920

a = list(map(int, input().split(' ')))

ascending = True
descending = True

# 1 2 3 4 5 6 7 8
for i in range(1, 8):
    if a[i] > a[i - 1]:
        descending = False
    elif a[i] < a[i - 1]:
        ascending = False

if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")
