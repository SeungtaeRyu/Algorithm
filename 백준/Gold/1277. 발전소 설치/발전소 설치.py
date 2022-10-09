import sys
input = sys.stdin.readline

n, w  = map(int, input().split())

m = float(input())

dot = dict()
adj = {i: [] for i in range(1, n+1)}

for i in range(1, n+1):
    dot[i] = tuple(map(int, input().split()))

for _ in range(w):
    a, b = map(int, input().split())
    adj[a].append((b, 0))
    adj[b].append((a, 0))

for i in range(1, n):
    for j in range(i+1, n+1):
        d = ((dot[i][0] - dot[j][0])**2 + (dot[i][1] - dot[j][1])**2)**(1/2)
        if d <= m:
            adj[i].append((j, d))
            adj[j].append((i, d))

visited = [False for _ in range(n+1)]
dij = [sys.maxsize for _ in range(n+1)]

visited[1] = True
dij[1] = 0
now = 1
while not visited[n]:
    for nextt, price in adj[now]:
        dij[nextt] = min(dij[nextt], dij[now] + price)

    minV = sys.maxsize
    for i in range(1, n+1):
        if visited[i]:
            continue
        if minV > dij[i]:
            minV = dij[i]
            now = i

    visited[now] = True

print(f'{int(dij[n]*1000)}')