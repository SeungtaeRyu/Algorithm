n = int(input())

count = 0
for i in range(1, n+1):
    x = list(str(i))
    if len(x) == 1:
        count += 1
    else:
        d = int(x[1]) - int(x[0])
        for j in range(2, len(x)):
            if int(x[j]) - int(x[j-1]) != d:
                break
        else:
            count += 1

print(count)