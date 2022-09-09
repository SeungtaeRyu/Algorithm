import sys
input = sys.stdin.readline

n, d = map(int, input().split())

dp = [0] * 10001
for i in range(1, 10001):
    dp[i] = i
    
shortcut = []
for i in range(n):
    shortcut.append(list(map(int, input().split())))

shortcut.sort()

for start, end, distance in shortcut:
    dp[end] = min(dp[end], dp[start]+distance)
    for i in range(end, 10001):
        dp[i] = min(dp[i-1]+1, dp[i])

print(dp[d])
