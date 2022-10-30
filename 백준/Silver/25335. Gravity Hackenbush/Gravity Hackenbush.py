import sys
input = sys.stdin.readline

n, m = map(int, input().split())

for _ in range(n):
    input()

R_count, G_count, B_count = 0, 0, 0

for _ in range(m):
    v, w, c = input().split()
    if c == 'R':
        R_count += 1
    elif c == 'G':
        G_count += 1
    elif c == 'B':
        B_count += 1

player1 = R_count + G_count // 2 + G_count % 2
player2 = B_count + G_count // 2

if player1 > player2:
    print('jhnah917')
else:
    print('jhnan917')