import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

indegree = [0 for _ in range(n+1)]
rules = {i: [] for i in range(1, n+1)}

for _ in range(m):
    k, *singer_list = map(int, input().split())

    for i in range(k):
        for j in range(i+1, k):
            if singer_list[j] not in rules[singer_list[i]]:
                rules[singer_list[i]].append(singer_list[j])
                indegree[singer_list[j]] += 1

q = deque()
qq = []
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)


while q:
    now = q.popleft()
    qq.append(now)
    for nextt in rules[now]:
        indegree[nextt] -= 1
        if indegree[nextt] == 0:
            q.append(nextt)

if len(qq) == n:
    for i in qq:
        print(i)
else:
    print(0)