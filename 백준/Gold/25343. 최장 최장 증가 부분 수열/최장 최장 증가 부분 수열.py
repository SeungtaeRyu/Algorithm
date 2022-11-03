import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[1 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        maxdp = 1
        minvalue = 10001
        for k in range(i+1):
            for l in range(j+1):
                if arr[k][l] < arr[i][j]:
                    dp[i][j] = max(dp[k][l]+1, dp[i][j])

maxvalue = 0
for i in range(n):
    for j in range(n):
        maxvalue = max(maxvalue, dp[i][j])

print(maxvalue)