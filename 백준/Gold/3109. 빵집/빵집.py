import sys
input = sys.stdin.readline

def dfs(rr, cc):
    global count, flag
    if cc == c-1:
        flag = True
        count += 1
        return
    for n_r in range(rr-1, rr+2):
        if n_r < 0 or n_r == r:
            continue
        if visited[n_r][cc] == 0 and arr[n_r][cc] != 'x':
            visited[n_r][cc] = 1
            dfs(n_r, cc+1)
            if flag:
                return

r, c = map(int, input().split())

arr = [list(input().rstrip()) for _ in range(r)]
visited = [[0 for _ in range(c)] for _ in range(r)]

count = 0
for rr in range(r):
    flag = False
    dfs(rr, 1)

print(count)

