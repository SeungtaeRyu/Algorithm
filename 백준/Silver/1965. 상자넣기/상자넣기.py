n = int(input())
boxes = list(map(int, input().split()))

dp = [1 for i in range(n)]

for i in range(1,n):
    max_value = 0
    max_index = i
    for j in range(i):
        if boxes[i] > boxes[j] and dp[j] > max_value:
            max_value = dp[j]
            max_index = j
    if boxes[max_index] < boxes[i]:
        dp[i] += max_value
    
            
print(max(dp))