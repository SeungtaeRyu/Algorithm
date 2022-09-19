def f(index, s, e, info, lion):
    global max_ckdl
    global ans
    if index == 11:
        return
    if s == e:
        a_score = 0
        l_score = 0
        for i in range(11):
            if info[i] == 0 and lion[i] == 0:
                continue
            if info[i] < lion[i]:
                l_score += (10-i)
            else:
                a_score += (10-i)
        ckdl = l_score - a_score
        # print(info)
        # print(lion)
        # print(f'ans ={ans}')
        # print(f'lion={lion}')
        # print(f'어피치={a_score} 라이언={l_score} 차이={ckdl} 최대차이={max_ckdl}')
        # print()
        if ckdl > max_ckdl:
            max_ckdl = ckdl
            ans = lion[:]
        elif ckdl == max_ckdl:
            for i in range(10, -1, -1):
                if lion[i] == 0 and ans[i] == 0:
                    pass
                elif lion[i] > ans[i]:
                    ans = lion[:]
                    break
                else:
                    break
            return
        return
    else:
        # if lion[index] <= info[index]:
        lion[index] += 1
        f(index, s+1, e, info, lion)
        lion[index] -= 1
        f(index+1, s, e, info, lion)
        # else:
        #     f(index+1, s, e, info, lion)


def solution(n, info):
    global ans
    global max_ckdl
    max_ckdl = 1
    ans = [0] * 11
    lion = [0] * 11
    f(0,0,n,info,lion)
    if sum(ans) == 0:
        return [-1]
    else:
        return ans