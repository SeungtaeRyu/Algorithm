n, k = map(int, input().split())

dp = [0 for _ in range(100001)]
coin = []

for _ in range(n):
    c = int(input())
    dp[c] = 1
    coin.append(c)

for i in range(1, k+1):
    temp_list = []
    for c in coin:
        if i-c < 0 or dp[i-c] == -1:
            continue
        else:
            temp_list.append(dp[i-c]+1)
    if temp_list:
        dp[i] = min(temp_list)
    else:
        dp[i] = -1
print(dp[k])