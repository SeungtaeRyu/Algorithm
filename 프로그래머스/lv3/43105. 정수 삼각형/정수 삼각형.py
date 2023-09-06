def solution(triangle):
    answer = 0
    dp = [[0 for _ in range(len(triangle)+1)] for _ in range(len(triangle))]
    
    dp[0][1] = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(1, i+2):
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j-1]
    
    return max(dp[len(triangle)-1])