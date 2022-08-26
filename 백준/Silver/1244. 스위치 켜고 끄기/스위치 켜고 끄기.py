import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline
n = int(input())
switch = list(map(int, input().split()))

for _ in range(int(input())):
    sex, num = map(int, input().split())
    if sex == 1:
        x = num
        while x <= n:
            if switch[x-1]:
                switch[x-1] = 0
            else:
                switch[x-1] = 1
            x += num
    else:
        x = 1
        while num-1-x >= 0 and num-1+x < n:
            if switch[num-1-x] == switch[num-1+x]:
                x += 1
            else:
                break
        x -= 1
        for i in range(num-1-x, num+x):
            if switch[i]:
                switch[i] = 0
            else:
                switch[i] = 1
count = 0
for i in range(n):
    print(f'{switch[i]}', end=" ")
    count += 1
    if count == 20:
        print()
        count = 0