import sys
sys.stdin = open("input.txt")

# dfs 함수 정의
def dfs(x, y):
    global isdochak
    visited[x][y] = 1
    if arr[x][y] == 3:
        isdochak = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if visited[nx][ny] or arr[nx][ny] == 1:
            continue
        else:
            dfs(nx, ny)

# direction 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 테스트 케이스  만큼 반복 동작
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [[1] * (n+2)] + [[1]+list(map(int, list(input()))) +[1] for _ in range(n)] + [[1] * (n+2)]

    visited = [[0 for _ in range(n+2)] for _ in range(n+2)]

    # 시작점을 찾는 코드
    for i in range(n+2):
        for j in range(n+2):
            if arr[i][j] == 2:
                x, y = i, j
    isdochak = 0

    dfs(x, y)
    print(f'#{tc} {isdochak}')