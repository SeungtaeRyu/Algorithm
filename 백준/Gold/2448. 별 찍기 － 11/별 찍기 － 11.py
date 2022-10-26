def star11(k, cnt):
    if k == n:
        return
    else:
        temp = ans[:]
        for i in range(len(temp)):
            ans[i] = ' ' * k + temp[i] + ' ' * k
        for i in range(len(temp)):
            ans.append(temp[i] + ' ' + temp[i])

        star11(3 * (2 ** cnt), cnt+1)

n = int(input())

ans = ['  *  ', ' * * ', '*****']

star11(3, 1)

for i in ans:
    print(i)