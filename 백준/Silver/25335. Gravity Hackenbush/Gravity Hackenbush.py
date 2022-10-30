import sys
input = sys.stdin.readline

n, m = map(int, input().split())

for _ in range(n):
    input()

R_count, G_count, B_count = 0, 0, 0
count_dic = {'R': 0, 'G': 0, 'B': 0}

for _ in range(m):
    v, w, c = input().split()

    count_dic[c] += 1

player1 = count_dic['R'] + count_dic['G'] // 2 + count_dic['G'] % 2
player2 = count_dic['B'] + count_dic['G'] // 2

if player1 > player2:
    print('jhnah917')
else:
    print('jhnan917')