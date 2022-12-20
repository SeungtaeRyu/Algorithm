import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    n = int(input())
    start_r, start_c = map(int, input().split())
    store = []
    for _ in range(n):
        store.append(tuple(map(int, input().split())))
    end_r, end_c = map(int, input().split())
    visited = [0 for _ in range(n)]
    flag = False
    stack = deque([(start_r, start_c)])
    while stack:
        x, y = stack.popleft()
        if abs(x-end_r) + abs(y-end_c) <= 1000:
            flag = True
            break
        for i in range(n):
            if visited[i]:
                continue
            if abs(x-store[i][0]) + abs(y-store[i][1]) <= 1000:
                visited[i] = 1
                stack.append((store[i][0], store[i][1]))
    if flag:
        print("happy")
    else:
        print("sad")
