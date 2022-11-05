import sys
input = sys.stdin.readline

n = int(input())

stack = []
for i in range(n):
    info = list(input().split())
    if info[0] == 'push':
        stack.append(int(info[1]))
    if info[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    if info[0] == 'size':
        print(len(stack))
    if info[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    if info[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)