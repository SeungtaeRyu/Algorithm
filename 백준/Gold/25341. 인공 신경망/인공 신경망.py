import sys
input = sys.stdin.readline

n, m, q = map(int, input().split())

info = []
for i in range(m):
    info.append(list(map(int, input().split())))

end = tuple(map(int, input().split()))

A_VALUE = [0 for i in range(n)]
temp = end[-1]
for j in range(len(info)):
    temp += end[j] * info[j][-1]
    for k in range(info[j][0]):
        A_VALUE[info[j][1+k]-1] += end[j] * info[j][1+k+info[j][0]]

for i in range(q):
    total = temp
    A_KEY = list(map(int, input().split()))
    for i in range(n):
        total += A_KEY[i] * A_VALUE[i]
    print(total)