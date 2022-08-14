a = input()
b = input()

LCS = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] != b[j]:
            LCS[i+1][j+1] = max(LCS[i][j+1], LCS[i+1][j])
        else:
            LCS[i+1][j+1] = LCS[i][j]+1

print(LCS[-1][-1])

x, y = len(a), len(b)
LCSword = ''
while x > 0 and y > 0:
    if LCS[x][y] == LCS[x-1][y]:
        x -= 1
    elif LCS[x][y] == LCS[x][y-1]:
        y -= 1
    else:
        LCSword = a[x-1] + LCSword
        x -= 1
        y -= 1
print(LCSword)