import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())

indegree = [0 for _ in range(n+1)]
rules = {i: [] for i in range(1, n+1)}

for i in range(m):
    a, b = map(int, input().split())
    indegree[b] += 1
    rules[a].append(b)

hq = []
for i in range(1, n+1):
    if indegree[i] == 0:
       heapq.heappush(hq, i)

while hq:
    now = heapq.heappop(hq)
    print(now, end=" ")
    for nextt in rules[now]:
        indegree[nextt] -= 1
        if indegree[nextt] == 0:
            heapq.heappush(hq, nextt)
