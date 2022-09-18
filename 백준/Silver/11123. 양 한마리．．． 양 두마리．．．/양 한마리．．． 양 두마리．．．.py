import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(input().rstrip()) for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]

    count = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j] == '#':
                count += 1
                q = deque([(i, j)])
                visited[i][j] = True
                while q:
                    x, y = q.popleft()
                    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                        nx = x + dx
                        ny = y + dy
                        if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] or arr[nx][ny] != '#':
                            continue
                        q.append((nx, ny))
                        visited[nx][ny] = True
    print(count)