import sys
dp = [[1, 0], [0, 1]]


def fib(n):
    if n == 0 or n == 1:
        return
    for _ in range(n - 1):
        dp.append((dp[-1][0] + dp[-2][0], dp[-1][1] + dp[-2][1] ))
    return


input = sys.stdin.readline
T = int(input().rstrip())
case = [int(input().rstrip()) for _ in range(T)]
fib(max(case))
for c in case:
    print(dp[c][0], dp[c][1])