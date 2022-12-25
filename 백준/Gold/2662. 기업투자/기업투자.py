import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0 for _ in range(m)]]
dp = [[0 for _ in range(m)] for _ in range(n+1)]
root = [[[] for _ in range(m)] for _ in range(n+1)]

for _ in range(n):
    a, *b = map(int, input().split())
    arr.append(b)

for i in range(n+1):
    dp[i][0] = arr[i][0]
    root[i][0].append(i)

for j in range(1, m):
    for i in range(1, n+1):
        for k in range(i+1):
            if dp[i][j] < dp[k][j-1] + arr[i-k][j]:
                dp[i][j] = dp[k][j-1] + arr[i-k][j]
                root[i][j] = root[k][j-1] + [i-k]

print(dp[n][m-1])
print(*root[n][m-1])
