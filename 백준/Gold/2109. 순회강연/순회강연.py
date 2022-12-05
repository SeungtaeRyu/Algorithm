import sys, heapq
input = sys.stdin.readline

n = int(input())
info = []
for _ in range(n):
    p, d = map(int, input().split())
    info.append((d, p))

info.sort(key=lambda x: (x[0], -x[1]))

date = 1
total = 0
selected = []
for i in range(len(info)):
    if info[i][0] >= date:
        total += info[i][1]
        heapq.heappush(selected, info[i][1])
        date += 1
        continue
    elif info[i][0] + 1 == date:
        total += info[i][1]
        heapq.heappush(selected, info[i][1])
        total -= heapq.heappop(selected)
print(total)
