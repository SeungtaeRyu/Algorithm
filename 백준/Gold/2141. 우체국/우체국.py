import sys
input = sys.stdin.readline

n = int(input())

info = []
left = 0
right = 0
for i in range(n):
    x, a = map(int, input().split())
    right += a
    info.append((x, a))
info.sort()

minV = sys.maxsize
ans = -1
for X, A in info:
    right -= A
    if minV > abs(right-left):
        minV = abs(right-left)
        ans = X
    left += A
# print(minV)
print(ans)