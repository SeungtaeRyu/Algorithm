stack = []
postfix = ''
for i in input():
    if i.isalpha():
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
while stack:
    postfix += stack.pop()
print(postfix)