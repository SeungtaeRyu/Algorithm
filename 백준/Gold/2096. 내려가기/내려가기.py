import sys
input = sys.stdin.readline

n = int(input())

a, b, c = map(int, input().split())

maxV = [[a, b, c], [0, 0, 0]]
minV = [[a, b, c], [0, 0, 0]]

if n == 1:
    print(max(maxV[0]), min(minV[0]))
else:
    for i in range(1, n):
        a, b, c = map(int, input().split())
        maxV[1][0] = max(maxV[0][0], maxV[0][1]) + a
        maxV[1][1] = max(maxV[0]) + b
        maxV[1][2] = max(maxV[0][1], maxV[0][2]) + c
        maxV[0] = maxV[1][:]

        minV[1][0] = min(minV[0][0], minV[0][1]) + a
        minV[1][1] = min(minV[0]) + b
        minV[1][2] = min(minV[0][1], minV[0][2]) + c
        minV[0] = minV[1][:]
    print(max(maxV[0]), min(minV[0]))
