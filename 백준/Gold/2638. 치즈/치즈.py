import sys
input = sys.stdin.readline

r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]

cur = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] == 1:
            cur += 1

if cur == 0:
    print(0)
    exit()

count = 0
while True:
    visited = [[0 for _ in range(c)] for _ in range(r)]
    visited[0][0] = 1
    stack = [(0, 0)]
    while stack:
        x, y = stack.pop()
        if x - 1 >= 0:
            if not visited[x-1][y] and arr[x - 1][y] == 0:
                visited[x-1][y] = 1
                stack.append((x - 1, y))
            else:
                if not visited[x - 1][y]:
                    visited[x - 1][y] = 1
                else:
                    arr[x - 1][y] = 0

        if x + 1 < r:
            if not visited[x+1][y] and arr[x + 1][y] == 0:
                visited[x+1][y] = 1
                stack.append((x + 1, y))
            else:
                if not visited[x + 1][y]:
                    visited[x + 1][y] = 1
                else:
                    arr[x + 1][y] = 0

        if y - 1 >= 0:
            if not visited[x][y-1] and arr[x][y-1] == 0:
                visited[x][y-1] = 1
                stack.append((x, y-1))
            else:
                if not visited[x][y-1]:
                    visited[x][y-1] = 1
                else:
                    arr[x][y-1] = 0

        if y + 1 < c:
            if not visited[x][y+1] and arr[x][y+1] == 0:
                visited[x][y+1] = 1
                stack.append((x, y+1))
            else:
                if not visited[x][y+1]:
                    visited[x][y+1] = 1
                else:
                    arr[x][y+1] = 0
    count += 1
    cur = 0
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 1:
                cur += 1

    if cur == 0:
        print(count)
        break