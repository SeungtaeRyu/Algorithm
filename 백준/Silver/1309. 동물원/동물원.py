import sys
input = sys.stdin.readline

n = int(input())

dp = [[0 for _ in range(3)] for _ in range(n+1)]
dp_ans = [0] * (n+1)

dp_ans[0] = 1
for i in range(1, n+1):
    dp[i][0] = dp_ans[i-1]
    dp[i][1] = dp_ans[i-1] - dp[i-1][1]
    dp[i][2] = dp_ans[i-1] - dp[i-1][2]
    dp_ans[i] = (dp[i][0] + dp[i][1] + dp[i][2]) % 9901

print(dp_ans[n])