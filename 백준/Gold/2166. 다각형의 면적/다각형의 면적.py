import sys
input = sys.stdin.readline

dot = []

n = int(input())
for _ in range(n):
    dot.append(list(map(int, input().split())))

dot.append(dot[0])

plus = 0
minus = 0
for i in range(n):
    plus += dot[i][0]*dot[i+1][1]
    minus += dot[i][1]*dot[i+1][0]

print(f'{abs(plus-minus) / 2:.1f}')