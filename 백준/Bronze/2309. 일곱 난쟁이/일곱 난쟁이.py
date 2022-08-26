nanjaeng = [int(input()) for _ in range(9)]

def f(i, n, s):
    global flag
    if flag == True or s > 100:
        return
    if i == n:
        if s == 100 and sum(bit) == 7:
            for x in range(9):
                if bit[x]:
                    ans_list.append(nanjaeng[x])
            flag = True
            return
        else:
            return
    else:
        bit[i] = 1
        f(i+1, n, s + nanjaeng[i])
        bit[i] = 0
        f(i+1, n, s)

bit = [0] * 9
ans_list = []
flag = False
f(0, 9, 0)

ans_list.sort()
for nan in ans_list:
    print(nan)