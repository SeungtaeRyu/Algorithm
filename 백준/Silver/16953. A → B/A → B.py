from collections import deque
n, m = map(int, input().split())
def bfs(s):
    q = deque([[s, 1]])
    while q:
        now = q.popleft()
        temp = []
        temp.append(now[0] * 2)
        temp.append(int(str(now[0]) + '1'))

        for num in temp:
            if num == m:
                return now[1]+1
            elif num < m:
                q.append([num, now[1]+1])
    return -1
print(bfs(n))