import sys
from collections import defaultdict

input = sys.stdin.readline

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
s, a, b = map(int, input().split())

virus = defaultdict(list)
for i in range(n):
    for j in range(n):
        virus[arr[i][j]].append((i, j))
        if arr[i][j] != 0:
            visited[i][j] = 1

virus = sorted(virus.items())[1:]

count = 0
while count < s:
    for i in range(len(virus)):
        v = virus[i][0]
        v_list = virus[i][1]
        # print(v, v_list)
        temp = []
        while v_list:
            x, y = v_list.pop()
            if x - 1 >= 0 and visited[x - 1][y] == 0:
                visited[x - 1][y] = 1
                arr[x - 1][y] = v
                temp.append((x - 1, y))
            if x + 1 < n and visited[x + 1][y] == 0:
                visited[x + 1][y] = 1
                arr[x + 1][y] = v
                temp.append((x + 1, y))
            if y - 1 >= 0 and visited[x][y - 1] == 0:
                visited[x][y - 1] = 1
                arr[x][y - 1] = v
                temp.append((x, y - 1))
            if y + 1 < n and visited[x][y + 1] == 0:
                visited[x][y + 1] = 1
                arr[x][y + 1] = v
                temp.append((x, y + 1))
        virus[i] = (v, temp[:])
    count += 1

print(arr[a-1][b-1])