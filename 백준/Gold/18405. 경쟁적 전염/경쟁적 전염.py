import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
s, a, b = map(int, input().split())


if arr[a-1][b-1] != 0:
    print(arr[a-1][b-1])
else:
    stack = [(a-1, b-1)]
    ans = [0]
    count = 0
    while count < s and len(ans) == 1:
        temp = []
        while stack:
            x, y = stack.pop()
            if x - 1 >= 0 and visited[x - 1][y] == 0:
                visited[x - 1][y] = 1
                temp.append((x - 1, y))
                if arr[x - 1][y] != 0:
                    ans.append(arr[x - 1][y])
            if x + 1 < n and visited[x + 1][y] == 0:
                visited[x + 1][y] = 1
                temp.append((x + 1, y))
                if arr[x + 1][y] != 0:
                    ans.append(arr[x + 1][y])
            if y - 1 >= 0 and visited[x][y - 1] == 0:
                visited[x][y - 1] = 1
                temp.append((x, y - 1))
                if arr[x][y - 1] != 0:
                    ans.append(arr[x][y - 1])
            if y + 1 < n and visited[x][y + 1] == 0:
                visited[x][y + 1] = 1
                temp.append((x, y + 1))
                if arr[x][y + 1] != 0:
                    ans.append(arr[x][y + 1])
        stack = temp[:]
        count += 1

    if len(ans) == 1:
        print(0)
    else:
        print(min(ans[1:]))