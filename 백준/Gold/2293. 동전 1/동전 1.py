import sys
input = sys.stdin.readline
n, k = map(int, input().split())

dp = [0 for _ in range(k+1)]
coins = []
for i in range(n):
    coins.append(int(input()))

dp[0] = 1
for coin in coins:
    for i in range(1, k+1):
        if i-coin >= 0 :
            dp[i] += dp[i-coin]
print(dp[k])