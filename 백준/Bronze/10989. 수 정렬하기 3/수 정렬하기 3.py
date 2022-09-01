import sys
input = sys.stdin.readline

counting = [0] * 10001

for i in range(int(input())):
    counting[int(input())] += 1

for i in range(1, 10001):
    for j in range(counting[i]):
        print(i)

