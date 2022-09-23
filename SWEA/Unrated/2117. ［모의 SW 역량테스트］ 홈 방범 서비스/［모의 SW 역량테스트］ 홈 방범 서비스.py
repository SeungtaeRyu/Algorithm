from collections import deque

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_count = [0] * (40)
    for i in range(n):
        for j in range(n):
            visited = [[30 for _ in range(n)] for _ in range(n)]
            q = deque([(i, j)])
            visited[i][j] = 1
            while q:
                x, y = q.popleft()
                if visited[i][j] == 21:
                    break
                for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    nx = x + dx
                    ny = y + dy
                    if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] != 30:
                        continue
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))


            for k in range(1, 40):
                count = 0
                for a in range(n):
                    for b in range(n):
                        if arr[a][b] == 1 and visited[a][b] <= k:
                            count += 1
                max_count[k] = max(max_count[k], count)


    max_home = 0
    for k in range(1, 40):
        if max_count[k] * m >= (k*k + (k-1)*(k-1)):
            max_home = max(max_count[k], max_home)
    print(f'#{tc} {max_home}')
