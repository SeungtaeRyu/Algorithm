a = input()     # ABRACADABRA           길이 11
b = input()     # ECADADABRBCRDARA      길이 16

LCS = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]   # 0 ~ 11 x 0 ~ 15


for i in range(len(a)):                     # 0 ~ 10 까지 반복
    for j in range(len(b)):                 # 0 ~ 15 까지 반복
        if a[i] == b[j]:
            LCS[i+1][j+1] = LCS[i][j] + 1

max_value = 0
for k in range(1, len(LCS)):
    max_value = max(max_value, max(LCS[k]))
print(max_value)