import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
arr2 = [[0 for _ in range(m)] for _ in range(n)]
ans = [['0' for _ in range(m)] for _ in range(n)]
group_num = [[0 for _ in range(m)] for _ in range(n)]
group_count = 0

def dfs(x, y):
    if x - 1 >= 0 and visited[x - 1][y] == False and arr[x - 1][y] == 0:
        visited[x - 1][y] = True
        group.append((x - 1, y))
        dfs(x - 1, y)
    # 하
    if x + 1 < n and visited[x + 1][y] == False and arr[x + 1][y] == 0:
        visited[x + 1][y] = True
        group.append((x + 1, y))
        dfs(x + 1, y)
    # 좌
    if y - 1 >= 0 and visited[x][y - 1] == False and arr[x][y - 1] == 0:
        visited[x][y - 1] = True
        group.append((x, y - 1))
        dfs(x, y - 1)
    # 우
    if y + 1 < m and visited[x][y + 1] == False and arr[x][y + 1] == 0:
        visited[x][y + 1] = True
        group.append((x, y + 1))
        dfs(x, y + 1)

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 and visited[i][j] == False:
            group_count += 1
            visited[i][j] = True
            group = [(i, j)]
            dfs(i, j)
            g_length = len(group)
            for x, y in group:
                arr2[x][y] = g_length
                group_num[x][y] = group_count

for i in range(n):
    for j in range(m):
        if arr[i][j] != 0:
            total = 1
            group_list = []
            if i - 1 >= 0:
                group_list.append(group_num[i-1][j])
                total += arr2[i-1][j]
            # 하
            if i + 1 < n and group_num[i+1][j] not in group_list:
                group_list.append(group_num[i+1][j])
                total += arr2[i+1][j]
            # 좌
            if j - 1 >= 0 and group_num[i][j-1] not in group_list:
                group_list.append(group_num[i][j-1])
                total += arr2[i][j-1]
            # 우
            if j + 1 < m and group_num[i][j+1] not in group_list:
                group_list.append(group_num[i][j+1])
                total += arr2[i][j+1]

            ans[i][j] = str(total % 10)

for i in ans:
    print("".join(i))
