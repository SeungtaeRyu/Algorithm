import sys, heapq
input = sys.stdin.readline

n = int(input())

q = []
for i in range(n):
    q.append(tuple(map(int, input().split())))

q.sort(key=lambda x: (x[0], -x[1]))


date = 1
cup = 0
selected = []
for i in range(n):
    if date <= q[i][0]:
        cup += q[i][1]
        heapq.heappush(selected, q[i][1])
        date += 1
        continue
    if date - 1 <= q[i][0]:
        if selected[0] < q[i][1]:
            heapq.heappush(selected, q[i][1])
            cup += q[i][1]
            cup -= heapq.heappop(selected)
            # date += 1

print(cup)