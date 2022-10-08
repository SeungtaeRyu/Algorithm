import sys

input = sys.stdin.readline

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    visited = [False for _ in range(n + 1)]
    selected = [0] + list(map(int, input().split()))

    ans = n
    for i in range(1, n + 1):
        if selected[i] == i:
            visited[i] = True
            ans -= 1

    for i in range(1, n + 1):
        if visited[i]:
            continue
        j = i
        list1 = []
        while True:
            if visited[j] == True:
                count = 0
                while list1:
                    now = list1.pop()
                    count += 1
                    if now == j:
                        ans -= count
                        break
                break
            else:
                visited[j] = True
                list1.append(j)
                j = selected[j]
    print(ans)