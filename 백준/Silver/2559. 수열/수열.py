import sys
input = sys.stdin.readline

n, k = map(int, input().split())
numbers = list(map(int, input().split()))
ans = sum(numbers[:k])
temp = sum(numbers[:k])                         # temp = sum[0:5]
for i in range(0, n-k):                         # 10 5 => 0,1,2,3,4
    temp = temp - numbers[i] + numbers[k+i]     #
    ans = max(temp, ans)
print(ans)