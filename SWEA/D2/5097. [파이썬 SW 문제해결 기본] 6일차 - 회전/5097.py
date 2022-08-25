import sys
sys.stdin = open("input.txt")

from collections import deque

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))
    for _ in range(m):
        q.append(q.popleft())
    print(f'#{tc} {q.popleft()}')