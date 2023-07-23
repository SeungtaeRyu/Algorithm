from collections import defaultdict

def solution(k, tangerine):
    answer = 0

    c_dict = defaultdict(int)

    for t in tangerine:
        c_dict[t] += 1

    c_list = list(c_dict.values())
    c_list.sort(reverse=True)

    select = 0
    for i in c_list:
        select += i
        answer += 1
        if select >= k:
            break

    return answer