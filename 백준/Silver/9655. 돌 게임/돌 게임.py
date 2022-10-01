import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)

n = n % 4

if n == 0:
    print('CY')
if n == 1:
    print('SK')
if n == 2:
    print('CY')
if n == 3:
    print('SK')
