n = int(input())
code = input()
numbers = []
for i in range(n):
    numbers.append(input())
code_list = []
for i in code:
    if i.isalpha():
        code_list.append(numbers[ord(i)-65])
    else:
        code_list.append(i)
stack = []
for i in code_list:
    if i.isdecimal():
        stack.append(float(i))
    elif i == '*':
        stack.append(stack.pop() * stack.pop())
    elif i == '/':
        stack.append(1/stack.pop() * stack.pop())
    elif i == '+':
        stack.append(stack.pop() + stack.pop())
    elif i == '-':
        stack.append(-stack.pop() + stack.pop())
print(f'{stack[0]:.2f}')