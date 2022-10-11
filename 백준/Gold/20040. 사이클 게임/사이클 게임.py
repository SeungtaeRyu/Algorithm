import sys
input = sys.stdin.readline

n, m = map(int, input().split())

rep = [i for i in range(n)]
adj = {i: [i] for i in range(n)}

ans = 0
for _ in range(1, m+1):
    a, b = map(int ,input().split())

    if rep[a] == rep[b]:
        ans = _
        break
        
    if rep[a] < rep[b]:
        x = rep[b]
        while adj[x]:
            y = adj[x].pop()
            adj[rep[a]].append(y)
            rep[y] = rep[a]
    else:
        x = rep[a]
        while adj[x]:
            y = adj[x].pop()
            adj[rep[b]].append(y)
            rep[y] = rep[b]

print(ans)