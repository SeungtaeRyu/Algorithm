import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
baenang = []
for i in range(n):
    baenang.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        if (j-baenang[i-1][0]) < 0:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-baenang[i-1][0]] + baenang[i-1][1])

print(dp[n][k])