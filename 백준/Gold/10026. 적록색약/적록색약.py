import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def f1(x, y, value):
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n or visited1[nx][ny]:
            continue
        if value == arr[nx][ny]:
            visited1[nx][ny] = 1
            f1(nx, ny, value)

def f2(x, y, value):
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n or visited2[nx][ny]:
            continue
        if value == arr[nx][ny]:
            visited2[nx][ny] = 1
            f2(nx, ny, value)
        elif value == 'R' and arr[nx][ny] == 'G' or value == 'G' and arr[nx][ny] == 'R':
            visited2[nx][ny] = 1
            f2(nx, ny, value)

n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
visited1 = [[0 for _ in range(n)] for _ in range(n)]
visited2 = [[0 for _ in range(n)] for _ in range(n)]

count1 = 0
count2 = 0
for i in range(n):
    for j in range(n):
        if not visited1[i][j]:
            visited1[i][j] = 1
            count1 += 1
            f1(i, j, arr[i][j])
        if not visited2[i][j]:
            visited2[i][j] = 1
            count2 += 1
            f2(i, j, arr[i][j])

print(count1, count2)