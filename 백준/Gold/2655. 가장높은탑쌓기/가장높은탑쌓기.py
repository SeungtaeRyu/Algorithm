import sys
input = sys.stdin.readline

n = int(input())
byukdol = [(0,0,0,0)]
for i in range(n):
    area, h, w = map(int, input().split())
    byukdol.append((i+1, area, h, w))

byukdol.sort(key=lambda x: x[3])
dp = [0] * (n+1)
for i in range(0, n+1):
    for j in range(0, i):
        if byukdol[i][1] > byukdol[j][1]:
            dp[i] = max(dp[i], dp[j] + byukdol[i][2])
max_h = max(dp)
index = n
rst = []
while index != 0:
    # print(f' index = {index}, max_h = {max_h} ')
    if max_h == dp[index]:
        rst.append(byukdol[index][0])
        max_h -= byukdol[index][2]
    index -= 1
print(len(rst))
for i in range(len(rst)-1, -1, -1):
    print(rst[i])