import sys, heapq
input = sys.stdin.readline

n, h, t = map(int, input().split())

info = []
for i in range(n):
    heapq.heappush(info, -int(input()))

if info[0] > -h:
    print("YES")
    print(0)
    exit()

for i in range(1, t+1):
    x = -heapq.heappop(info)
    if x == 1:
        heapq.heappush(info, -x)
    else:
        x = x//2
        heapq.heappush(info, -x)
    if info[0] > -h:
        break

if info[0] > -h:
    print("YES")
    print(i)
else:
    print("NO")
    print(-info[0])