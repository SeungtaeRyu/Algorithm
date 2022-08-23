for tc in range(1, 11):
    n = int(input())

    stack = []

    # 후위표기식 변환
    postfix = ''
    for i in input():
        if i.isdecimal():
            postfix += i
        elif i == "(":
            stack.append(i)
        elif i == ")":
            while stack and stack[-1] != "(":
                postfix += stack.pop()
            stack.pop()
        elif i == "*" or i == "/":
            while stack and stack[-1] == "*" or stack and stack[-1] == "/":
                postfix += stack.pop()
            stack.append(i)
        elif i == "+" or i == "-":
            while stack and stack[-1] != "(":
                postfix += stack.pop()
            stack.append(i)
    for i in stack:
        postfix += i

    # 후위 표기식 계산
    for i in postfix:
        if i.isdecimal():
            stack.append(i)
        elif i == "*":
            stack.append(int(stack.pop()) * int(stack.pop()))
        elif i == "/":
            stack.append(1 / int(stack.pop()) * int(stack.pop()))
        elif i == "+":
            stack.append(int(stack.pop()) + int(stack.pop()))
        elif i == "-":
            stack.append(- int(stack.pop()) * int(stack.pop()))
    print(f'#{tc} {stack.pop()}')