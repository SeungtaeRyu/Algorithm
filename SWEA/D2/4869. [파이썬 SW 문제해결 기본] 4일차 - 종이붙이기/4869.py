import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    num = int(input())
    dp = [0 for _ in range(num//2)]
    dp[0] = 1
    dp[1] = 3
    for i in range(2, num//10):
        dp[i] = 2 * dp[i-2] + dp[i-1]
    print(f'#{tc} {dp[i]}')