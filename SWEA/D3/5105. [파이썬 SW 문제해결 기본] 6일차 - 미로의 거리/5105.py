import sys
sys.stdin = open("input.txt")

def dfs(x,y,s):
    global minV
    visited[x][y] = True
    for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] or arr[nx][ny] == '1':
            continue
        else:
            if arr[nx][ny] == '3':
                minV = min(minV, s)
            dfs(nx, ny, s+1)
    visited[x][y] = False


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == '2':
                x, y = i, j
    minV = n*n
    dfs(x, y, 0)
    if minV == n*n:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {minV}')