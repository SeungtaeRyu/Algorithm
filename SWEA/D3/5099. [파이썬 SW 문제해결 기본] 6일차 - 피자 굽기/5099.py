import sys
sys.stdin = open("input.txt")

from collections import deque
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    cheeze = list(map(int, input().split()))
    q = deque()
    index = 0
    for _ in range(n):
        q.append((cheeze[index], index+1))
        index += 1

    while len(q) > 1:
        x = q.popleft()
        if x[0] == 1 and index < m:
            q.append((cheeze[index], index+1))
            index += 1
        elif x[0] != 0:
            q.append((x[0]//2, x[1]))
    print(f'#{tc    } {q.popleft()[1]}')
