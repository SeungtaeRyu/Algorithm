import sys
input = sys.stdin.readline

n, e = map(int, input().split())
start = int(input())

adj = {i: [] for i in range(1, n+1)}
for _ in range(e):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))

dij = [sys.maxsize for _ in range(n+1)]
visited =[False for _ in range(n+1)]

dij[start] = 0
visited[start] = True
u = start
for _ in range(n-1):
    visited[u] = True
    for v, w in adj[u]:
        dij[v] = min(dij[v], dij[u] + w)

    minV = sys.maxsize
    for i in range(1, n+1):
        if visited[i] == False:
            if minV > dij[i]:
                minV = dij[i]
                u = i

for i in range(1, n+1):
    if dij[i] == sys.maxsize:
        print("INF")
    else:
        print(dij[i])

