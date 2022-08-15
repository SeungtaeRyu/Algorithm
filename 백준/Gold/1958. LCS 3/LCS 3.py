a = input()
b = input()
c = input()

LCS = [[[0 for _ in range(len(c)+1)] for _ in range(len(b)+1)] for _ in range(len(a)+1)]

for i in range(len(a)):
    for j in range(len(b)):
        for k in range(len(c)):
            if a[i] == b[j] == c[k]:
                LCS[i+1][j+1][k+1] = LCS[i][j][k] + 1
            else:
                LCS[i+1][j+1][k+1] = max(LCS[i][j+1][k+1], LCS[i+1][j][k+1], LCS[i+1][j+1][k])

print(LCS[-1][-1][-1])