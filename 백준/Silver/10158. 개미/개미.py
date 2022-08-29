import sys
input = sys.stdin.readline

w, h = map(int, input().split())

p, q = map(int, input().split())

t = int(input())

x = (t+p) % (2*w)
y = (t+q) % (2*h)

if x > w:
    x = 2*w - x
if y > h:
    y = 2*h - y

print(x, y)