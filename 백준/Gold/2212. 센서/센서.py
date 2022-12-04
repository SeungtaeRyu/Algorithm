import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
dot = list(map(int, input().split()))

if n == 1:
    print(0)
else:
    dot.sort()
    distance = []
    for i in range(n-1):
        distance.append(dot[i+1] - dot[i])

    ans = dot[-1] - dot[0]
    for _ in range(k-1):
        maxV = max(distance)
        ans -= maxV
        distance.remove(maxV)

    print(ans)
