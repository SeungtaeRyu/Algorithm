def star(k):
    if k == n:
        return
    else:
        temp = ans[:]
        ans[0] = temp[0] + '****'
        ans[1] = temp[1] + '    '
        ans[2] = '* ' + temp[0] + '**'
        for i in range(1, len(temp)):
            if i < len(temp) - 2:
                ans[2+i] = '* ' + temp[i] + ' *'
            else:
                ans.append('* ' + temp[i] + ' *')

        ans.append(temp[1] + '   *')
        ans.append(temp[0] + '****')

        star(k+1)

n = int(input())

if n == 1:
    print('*')
else:
    ans = []
    ans.append('*****')
    ans.append('*    ')
    ans.append('* ***')
    ans.append('* * *')
    ans.append('* * *')
    ans.append('*   *')
    ans.append('*****')
    star(2)
    for i in ans:
        print(i.rstrip())