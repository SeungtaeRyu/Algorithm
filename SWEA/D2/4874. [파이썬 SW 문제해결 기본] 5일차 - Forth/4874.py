import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    code = list(input().split())

    stack = []
    for i in code:
        if i.isdecimal():                           # 숫자가 들어오면 스택에 추가
            stack.append(i)
        elif i == '+' and len(stack) >= 2:          # 연산자가 들어오면 스택에 숫자가 2개이상 있는지 확인 후 연산
            y = int(stack.pop())
            x = int(stack.pop())
            stack.append(x + y)
        elif i == '-' and len(stack) >= 2:
            y = int(stack.pop())
            x = int(stack.pop())
            stack.append(x-y)
        elif i == '*' and len(stack) >= 2:
            y = int(stack.pop())
            x = int(stack.pop())
            stack.append(x*y)
        elif i == '/' and len(stack) >= 2:
            y = int(stack.pop())
            x = int(stack.pop())
            stack.append(x/y)
        elif i == '.' and len(stack) == 1:          # . 이 들어오면 스택에 숫자가 1개만 남았는지 확인 후 출력
            print(f'#{tc} {int(stack.pop())}')
        else:                                       # 위의 경우가 모두 아니면 에러처리
            print(f'#{tc} error')
            break