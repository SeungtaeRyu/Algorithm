import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(x, y):
    visited[x][y] = 1
    for dx, dy in [[0,1], [0,-1], [1,0], [-1,0]]:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[nx][ny] or arr[nx][ny] == 0:
            continue
        dfs(nx, ny)

T = int(input())
for tc in range(1, T+1):
    m, n, k = map(int, input().split())
    arr = [[0 for _ in range(n)] for _ in range(m)]
    visited = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(k):
        x, y = map(int, input().split())
        arr[x][y] = 1

    count = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1 and visited[i][j] == 0:
                count += 1
                visited[i][j] = 1
                dfs(i, j)

    print(count)