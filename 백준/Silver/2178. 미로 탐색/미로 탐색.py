from collections import deque

def bfs(x, y):
    visited[x][y] = 1
    q = deque()
    q.append([x, y])
    while q:
        t = q.popleft()
        if t[0] == n-1 and t[1] == m-1:
            break
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx = t[0] + dx
            ny = t[1] + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] or arr[nx][ny] == "0":
                continue
            else:
                q.append((nx, ny))
                visited[nx][ny] = visited[t[0]][t[1]] + 1

n, m = map(int, input().split())

arr = [list(input()) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

bfs(0, 0)
print(visited[n-1][m-1])