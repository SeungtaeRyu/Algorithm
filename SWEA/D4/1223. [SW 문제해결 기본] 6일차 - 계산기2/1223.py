import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    _ = input()
    cal = input()
    stack = []
    num = ''

    for i in cal:
        if i.isdecimal():
            num += i
        elif i == "+":
            while stack:
                num += stack.pop()
            stack.append(i)
        elif i == "*":
            stack.append(i)
    while stack:
        num += stack.pop()

    for i in num:
        if i.isdecimal():
            stack.append(i)
        else:
            if i == "*":
                y = stack.pop()
                x = stack.pop()
                stack.append(int(x) * int(y))
            elif i == "+":
                y = stack.pop()
                x = stack.pop()
                stack.append(int(x) + int(y))
    print(f'#{tc} {stack.pop()}')