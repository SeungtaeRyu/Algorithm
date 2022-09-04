import sys
input = sys.stdin.readline

c, n = map(int, input().split())

promotion = []
for i in range(n):
    price, client = map(int, input().split())
    promotion.append((client, price, client/price))

promotion.sort(key=lambda x: (-x[2], x[0]))

dp = [0] * 1001
for i in range(len(promotion)):
    for j in range(1, 1001):
        if i == 0:
            if j % promotion[i][0] == 0:
                dp[j] = (j // promotion[i][0]) * promotion[i][1]
            else:
                dp[j] = ((j // promotion[i][0]) + 1) * promotion[i][1]
        else:
            if j - promotion[i][0] < 0:
                dp[j] = min(dp[j], promotion[i][1])
            else:
                dp[j] = min(dp[j], dp[j-promotion[i][0]] + promotion[i][1])
print(dp[c])