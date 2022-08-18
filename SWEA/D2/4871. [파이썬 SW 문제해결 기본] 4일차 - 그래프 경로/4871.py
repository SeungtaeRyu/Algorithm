import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split())
    adj = [[] for _ in range(v+1)]
    visited = [False for _ in range(v+1)]

    for i in range(e):
        s, g = map(int, input().split())
        adj[s].append(g)
    start, find_g = map(int, input().split())

    stack = []
    stack.append(start)
    visited[start] = True
    while True:
        for node in adj[start]:
            if visited[node]:
                continue
            else:
                visited[node] = True
                stack.append(node)
                start = node
                break
        else:
            if stack:
                start = stack.pop()
            else:
                break
    if visited[find_g]:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')


