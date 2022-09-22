import sys
input = sys.stdin.readline

def f(n):
    if n <= 1:
        return 1
    else:
        return n * f(n-1)

T = int(input())
for tc in range(1, T+1):
    r, n = map(int, input().split())

    print(int(f(n)/(f(n-r)*f(r))))
