import sys
sys.stdin = open("input.txt")

from collections import deque

def bfs(v):
    q = deque([v])
    visited[v] = 1
    while q:
        now = q.popleft()
        for next in dict[now]:
            if next == g:
                return visited[now]
            if not visited[next]:
                q.append(next)
                visited[next] = visited[now] + 1
    return 0


T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split())
    visited = [0 for _ in range(v+1)]
    dict = {i: [] for i in range(1, v+1)}
    for i in range(e):
        x, y = map(int, input().split())
        dict[x].append(y)
        dict[y].append(x)

    s, g = map(int, input().split())
    print(f'#{tc} {bfs(s)}')