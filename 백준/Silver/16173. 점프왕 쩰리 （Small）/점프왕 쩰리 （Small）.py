import sys
input = sys.stdin.readline

def dfs(x, y):
    global flag
    num = arr[x][y]
    if num == 0:
        return
    if num == -1:
        flag = True
        return
    if x+num < n:
        dfs(x+num, y)
    if y+num < n:
        dfs(x, y+num)
    pass

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

flag = False
dfs(0, 0)

if flag:
    print("HaruHaru")
else:
    print("Hing")
