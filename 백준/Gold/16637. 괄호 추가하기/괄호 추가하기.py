from collections import deque

def f(i):
    global sik
    if i == n//2:
        temp1 = deque(sik[:])

        for j in range(n//2):
            if bracket[j]:
                x = int(temp1[2*j])
                y = int(temp1[2*j+2])
                if temp1[2*j+1] == '+':
                    temp1[2*j+2] = str(x + y)
                elif temp1[2*j+1] == '-':
                    temp1[2*j+2] = str(x - y)
                elif temp1[2*j+1] == '*':
                    temp1[2*j+2] = str(x * y)
                temp1[2*j] = 'x'
                temp1[2*j+1] = 'x'

        result = int(temp1[0])
        while temp1:
            giho = temp1.popleft()
            if giho == '+':
                while True:
                    num = temp1.popleft()
                    if num.isdecimal() or len(num) == 2:
                        break
                result += int(num)
            if giho == '-':
                while True:
                    num = temp1.popleft()
                    if num.isdecimal() or len(num) == 2:
                        break
                result -= int(num)
            if giho == '*':
                while True:
                    num = temp1.popleft()
                    if num.isdecimal() or len(num) == 2:
                        break
                result *= int(num)
        ans.append(result)
        return
    else:
        if bracket[i-1]:
            f(i+1)
        else:
            bracket[i] = 1
            f(i+1)
            bracket[i] = 0
            f(i+1)

n = int(input())
sik = list(input())

bracket = [0 for _ in range(n//2)]
ans = []

if n == 1:
    print(int(sik[0]))
else:
    f(1)
    print(max(ans))
