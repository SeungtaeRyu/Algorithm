import sys
input = sys.stdin.readline

n, m = map(int, input().split())

x = [0]
y = [0]
for _ in range(int(input())):
    i, j = map(int, input().split())
    if i == 0:
        x.append(j)
    else:
        y.append(j)
x.sort()
y.sort()
x.append(m)
y.append(n)

cur_x = 0
cur_y = 0
ans = 0
for i in range(1, len(x)):
    cur_x = x[i] - x[i-1]
    for j in range(1, len(y)):
        cur_y = y[j] - y[j-1]
        ans = max(ans, cur_x * cur_y)
print(ans)