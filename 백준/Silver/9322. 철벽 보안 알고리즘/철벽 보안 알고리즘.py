t = int(input())
for i in range(t):
    n = int(input())
    s = []
    for j in range(3):
        s.append(input().split())
    s_num = []
    for k in range(n):
        s_num.append(s[1].index(s[0][k]))
    for n in s_num:
        print(s[2][n], end=' ')