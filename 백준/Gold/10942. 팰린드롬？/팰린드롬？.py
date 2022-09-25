import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for i in range(n-1):
    if nums[i] == nums[i+1]:
        dp[i][i+1] = 1

for gap in range(2, n):           # 갭
    for start in range(0, n-gap):         # 시작점
        if nums[start] == nums[start+gap]:
            dp[start][start+gap] = dp[start+1][start+gap-1]

for _ in range(int(input())):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])
