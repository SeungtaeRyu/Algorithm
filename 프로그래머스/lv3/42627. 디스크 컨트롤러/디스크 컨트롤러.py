# import heapq

def solution(jobs):
    answer = 0
    n = len(jobs)
    # heapq.heapify(jobs)
    jobs.sort()

    answer = 0
    current = 0
    while jobs:
        if jobs[0][0] > current:
            current += jobs[0][0] - current
            continue

        i = 0
        select = 1000
        select_i = 0
        while i != len(jobs) and jobs[i][0] <= current:
            if jobs[i][1] < select:
                select = jobs[i][1]
                select_i = i
            i += 1
        x, y = jobs.pop(select_i)
        # print("x y", x, y)
        current += y
        answer += current - x
        # print("answer current",answer, current)

    # print(answer)
    return answer // n