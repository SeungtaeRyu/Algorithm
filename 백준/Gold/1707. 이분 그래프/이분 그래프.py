import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

k = int(input())

def dfs(u, cur, next):
    global flag
    for w in adj[u]:
        if visited[w] == -1:
            visited[w] = next
            dfs(w, next, cur)
        elif visited[w] == cur:
            flag = False
            return

for tc in range(k):
    v, e = map(int, input().split())
    adj = defaultdict(list)
    for _ in range(e):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    visited = [-1 for _ in range(v+1)]
    flag = True

    for i in range(1, v+1):
        if visited[i] == -1:
            visited[i] = 0
            dfs(i, 0, 1)

    if flag:
        print("YES")
    else:
        print("NO")