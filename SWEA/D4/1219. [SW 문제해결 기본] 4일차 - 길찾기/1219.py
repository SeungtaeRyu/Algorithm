import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    _, edge_count = map(int, input().split())
    adj = [[] for _ in range(100)]
    visited = [False for _ in range(100)]

    edge = list(map(int, input().split()))
    for i in range(edge_count):
        adj[edge[2*i]].append(edge[2*i+1])

    stack = []
    start = 0
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
    if visited[99]:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')