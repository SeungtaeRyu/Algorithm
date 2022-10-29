import sys
input = sys.stdin.readline

n = int(input())
t = list(map(int, input().split()))

maxT = max(t)
for i in range(maxT, sys.maxsize, maxT):
    for j in range(len(t)):
        if i % t[j] == 0:
            continue
        break
    else:
        break
print(i)