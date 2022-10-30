import sys
input = sys.stdin.readline

a, b, c, d = map(int, input().split())

n = int (input())

pants = []

for i in range(n):
    pants.append(tuple(map(int, input().split())))

dulle_to_length = [0 for _ in range(10001)]

x = b
while (a*(x-b)**2) + c >= d:
    dulle_to_length[(a*(x-b)**2) + c] = x
    x += 1

count = 0
for dulle, length in pants:
    if dulle_to_length[dulle] == length:
        count += 1

print(count)