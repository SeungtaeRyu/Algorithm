import sys
input = sys.stdin.readline

n = int(input())
info = []
for _ in range(n):
    age, name = input().split()
    info.append([int(age), _, name])

info.sort()
for i in range(n):
    print(f'{info[i][0]} {info[i][2]}')