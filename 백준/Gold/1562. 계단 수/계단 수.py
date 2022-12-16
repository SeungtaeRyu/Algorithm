n = int(input())

dp = [[0,0,0,0] for _ in range(10)]

for i in range(10):
    if i == 0:
        dp[i] = [0, 0, 0, 0]
    elif i == 9:
        dp[i] = [0, 0, 1, 0]
    else:
        dp[i] = [1, 0, 0, 0]

for i in range(2, n+1):
    temp = [[0,0,0,0] for _ in range(10)]
    for j in range(10):
        if j == 0:
            temp[j] = [0, dp[1][0] + dp[1][1], 0, dp[1][2] + dp[1][3]]
        elif j == 9:
            temp[j] = [0, 0, dp[8][0] + dp[8][2], dp[8][1] + dp[8][3]]
        else:
            temp[j] = [dp[j-1][0] + dp[j+1][0], dp[j-1][1] + dp[j+1][1], dp[j-1][2] + dp[j+1][2], dp[j-1][3] + dp[j+1][3]]
    dp = temp[:]

print((dp[0][3] + dp[1][3] + dp[2][3] + dp[3][3] + dp[4][3] + dp[5][3] + dp[6][3] + dp[7][3] + dp[8][3] + dp[9][3]) % 1000000000)