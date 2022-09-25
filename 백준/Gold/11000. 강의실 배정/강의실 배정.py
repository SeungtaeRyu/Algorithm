import sys
input = sys.stdin.readline

s = []
e = []
for i in range(int(input())):
    start, end = map(int, input().split())
    s.append(start)
    e.append(end)
s.sort()
e.sort()

max_count = 0
count = 0

s_i = 0
e_i = 0
while s_i < len(s):
    if s[s_i] < e[e_i]:
        count += 1
        s_i += 1
        max_count = max(max_count, count)
    else:
        count -= 1
        e_i += 1
print(max_count)


