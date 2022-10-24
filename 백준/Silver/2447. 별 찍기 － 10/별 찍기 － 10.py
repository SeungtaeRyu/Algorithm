def star(k, cnt):
    if k == n:
        return
    else:
        list1 = list2[:]
        for i in range(len(list1)):
            list2[i] = list1[i] * 3
        for i in range(len(list1)):
            list2.append(list1[i] + ' ' * (3**cnt) + list1[i])
        for i in range(len(list1)):
            list2.append(list2[i])

        star(k*3, cnt+1)
    pass


list2 = ['***', '* *', '***']

n = int(input())
star(3, 1)

for i in list2:
    print(i)