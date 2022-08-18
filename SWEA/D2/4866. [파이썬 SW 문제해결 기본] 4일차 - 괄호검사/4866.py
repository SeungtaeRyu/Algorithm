import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    word = input()
    stack = []
    for w in word:
        if not stack:
            if w == ')' or w == '}':
                stack.append(0)
                break
        if w == '{':
            stack.append(w)
        elif w == '(':
            stack.append(w)
        elif w == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                stack.append(0)
                break
        elif w == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(0)
                break
    if stack:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')