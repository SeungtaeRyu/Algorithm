import sys
input = sys.stdin.readline

def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        temp = 1
        while temp <= n:
            temp *= 2
        temp //= 2
        return f(n-temp) + count_list[temp-1] + (n-(temp-1))

a, b = map(int, input().split())

count_list = {}
maxsize = 10**16
count_list[1] = 1
temp = 3
plus = 2
while temp <= maxsize:
    count_list[temp] = count_list[((temp+1) // 2) - 1] * 2 + plus
    temp = (temp+1) * 2 - 1
    plus *= 2

print(f(b) - f(a-1))