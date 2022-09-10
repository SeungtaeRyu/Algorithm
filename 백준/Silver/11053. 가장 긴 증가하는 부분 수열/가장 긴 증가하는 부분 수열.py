import sys
input = sys.stdin.readline

n = int(input())
numbers = [0] + list(map(int, input().split()))

dp = [0] * (n+1)
for i in range(1, n+1):
    for j in range(i-1,-1,-1):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))