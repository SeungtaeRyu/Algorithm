import sys
from collections import deque
input = sys.stdin.readline

while True:
    w, h = map(int, input().split())

    if w == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False for _ in range(w)] for _ in range(h)]

    count = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and arr[i][j]:
                count += 1
                q = deque([(i, j)])
                visited[i][j] = True
                while q:
                    x, y = q.popleft()
                    for dx, dy in [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]:
                        nx = x + dx
                        ny = y + dy
                        if nx < 0 or nx >= h or ny < 0 or ny >= w or visited[nx][ny] or arr[nx][ny] == 0:
                            continue
                        q.append((nx, ny))
                        visited[nx][ny] = True
    print(count)