import sys

n, m = map(int, input().split())

no_listen = []
no_see = []

for _ in range(n):
    no_listen.append(sys.stdin.readline().rstrip())

for _ in range(m):
    no_see.append(sys.stdin.readline().rstrip())

no_see_listen = sorted(list(set(no_listen) & set(no_see)))

print(len(no_see_listen))
for name in no_see_listen:
    print(name)
