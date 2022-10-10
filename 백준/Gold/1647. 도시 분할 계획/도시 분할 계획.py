import sys, heapq
input = sys.stdin.readline

n, m = map(int ,input().split())

info = []

for _ in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(info, (c, a, b))

adj = {i: [i] for i in range(1, n+1)}
rep = [i for i in range(n+1)]

edge_count = 0
total = 0
while edge_count < n-2:
    c, a, b = heapq.heappop(info)

    if rep[a] == rep[b]:
        continue

    if rep[a] < rep[b]:
        y = rep[b]
        while adj[y]:
            x = adj[y].pop()
            rep[x] = rep[a]
            adj[rep[a]].append(x)

    else:
        y = rep[a]
        while adj[y]:
            x = adj[y].pop()
            rep[x] = rep[b]
            adj[rep[b]].append(x)

    total += c
    edge_count += 1
print(total)