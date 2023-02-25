import sys
input = sys.stdin.readline

def dfs(c):
    global count
    visited[c] = 1
    count += 1
    for n in adj[c]:
        if not visited[n]:
            dfs(n)

e = int(input())
v = int(input())

adj = {i: [] for i in range(1, e+1)}
visited = [0 for i in range(e+1)]
count = -1

for i in range(v):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

dfs(1)
print(count)