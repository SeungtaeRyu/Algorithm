import sys
input = sys.stdin.readline

n = int(input())
A = [0]
B = [0]
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

for i in range(1, n+1):
    for j in range(i+1, n+1):
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]
            B[i], B[j] = B[j], B[i]

dp = [0 for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(i-1, -1, -1):
        if B[i] > B[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))