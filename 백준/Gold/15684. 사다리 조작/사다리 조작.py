import sys
input = sys.stdin.readline

def check():
    end = [i for i in range(1, c + 1)]
    for i in range(r):
        for j in range(1, c):
            if arr[i][j]:
                end[j-1], end[j] = end[j], end[j-1]
    return start == end

def dfs(x, y, count):
    global ans
    if check():
        ans = min(ans, count)

    if count == 3 or count == ans:
        return
    
    else:
        while x < r:
            if arr[x][y-1] == 0 and arr[x][y] == 0 and arr[x][y+1] == 0:
                arr[x][y] = 1
                dfs(x, y, count + 1)
                arr[x][y] = 0
            if y == c-1:
                x += 1
                y = 1
            else:
                y += 1


if __name__ == '__main__':
    c, n, r = map(int, input().split())
    arr = [[0 for _ in range(c+1)] for _ in range(r)]

    start = [i for i in range(1, c + 1)]

    for i in range(n):
        a, b = map(int, input().split())
        arr[a-1][b] = 1

    if check():
        print(0)
    else:
        ans = 4
        dfs(0, 1, 0)
        if ans == 4:
            print(-1)
        else:
            print(ans)