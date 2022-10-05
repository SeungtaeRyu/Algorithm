# 위상정렬 개꿀
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

indegree = [0 for _ in range(n+1)]
rules = {i: [] for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int, input().split())
    rules[a].append(b)
    indegree[b] += 1

q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    print(now, end=" ")
    for nextt in rules[now]:
        indegree[nextt] -= 1
        if indegree[nextt] == 0:
            q.append(nextt)
