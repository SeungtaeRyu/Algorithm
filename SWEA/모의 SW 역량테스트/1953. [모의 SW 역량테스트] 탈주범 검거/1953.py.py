import sys
from collections import deque
sys.stdin =open('1953.txt')

def top(x, y):          # 위 칸이 1,2,5,6 이면 return 1, else return 0
    nx, ny = x - 1, y
    if nx >= 0 and (arr[nx][ny] == 1 or arr[nx][ny] == 2 or arr[nx][ny] == 5 or arr[nx][ny] == 6):
        return 1
    return 0

def bottom(x, y):       # 아래 칸이 1,2,4,7 이면 return 1, else return 0
    nx, ny = x + 1, y
    if nx < n and (arr[nx][ny] == 1 or arr[nx][ny] == 2 or arr[nx][ny] == 4 or arr[nx][ny] == 7):
        return 1
    return 0

def left(x, y):         # 왼쪽 칸이 1,3,4,5 이면 return 1, else return 0
    nx, ny = x, y - 1
    if ny >= 0 and (arr[nx][ny] == 1 or arr[nx][ny] == 3 or arr[nx][ny] == 4 or arr[nx][ny] == 5):
        return 1
    return 0

def right(x, y):        # 오른쪽 칸이 1,3,6,7 이면 return 1, else return 0
    nx, ny = x, y + 1
    if ny < m and (arr[nx][ny] == 1 or arr[nx][ny] == 3 or arr[nx][ny] == 6 or arr[nx][ny] == 7):
        return 1
    return 0

def bfs(now):
    stack = deque([now])
    visited[now[0]][now[1]] = 1
    while stack:
        x, y = stack.popleft()
        for dx, dy in [[-1,0],[1,0],[0,-1],[0,1]]:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >=n or ny < 0 or ny >= m or visited[nx][ny] or arr2[nx][ny] == 0:
                continue
            visited[nx][ny] = visited[x][y] + 1
            stack.append((nx, ny))

    pass

T = int(input())
for tc in range(1, T+1):
    n, m, startN, startM, t = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    arr2 = [[0 for _ in range(m)] for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if arr[x][y] == 1:
                arr2[x][y] = max(top(x, y), bottom(x, y), left(x, y), right(x, y))
            elif arr[x][y] == 2:
                arr2[x][y] = max(top(x, y), bottom(x, y))
            elif arr[x][y] == 3:
                arr2[x][y] = max(left(x, y), right(x, y))
            elif arr[x][y] == 4:
                arr2[x][y] = max(top(x, y), right(x, y))
            elif arr[x][y] == 5:
                arr2[x][y] = max(bottom(x, y), right(x, y))
            elif arr[x][y] == 6:
                arr2[x][y] = max(bottom(x, y), left(x, y))
            elif arr[x][y] == 7:
                arr2[x][y] = max(top(x, y), left(x, y))
    # for i in arr2:
    #     print(i)
    # print()

    visited = [[0 for _ in range(m)] for _ in range(n)]
    bfs((startN, startM))

    # for i in visited:
    #     print(i)
    # print()

    count = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] != 0 and visited[i][j] <= t:
                count += 1
    print(f'#{tc} {count}')