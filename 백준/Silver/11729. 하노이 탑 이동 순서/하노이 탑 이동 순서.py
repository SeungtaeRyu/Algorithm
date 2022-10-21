import sys
input = sys.stdin.readline

def f(x, y, n):
    if n == 1:
        return (x, y)
    else:
        z = 6 - x - y
        return f(x, z, n-1) + (x, y) + f(z, y, n-1)


n = int(input())

ans = f(1, 3, n)

print(len(ans)//2)
for i in range(len(ans)//2):
    print(f'{ans[2*i]} {ans[2*i+1]}')