def solution(info, queries):
    answer = []

    info_dict = {}

    for lang in ['cpp', 'java', 'python', "-"]:
        for job in ['backend', 'frontend', "-"]:
            for career in ['junior', 'senior', "-"]:
                for food in ['chicken', 'pizza', "-"]:
                    info_dict[lang + job + career + food] = []

    for i in info:
        infom = i.split()

        for lang in [infom[0],'-']:
            for end in [infom[1],'-']:
                for period in [infom[2], '-']:
                    for food in [infom[3], '-']:
                        info_dict[lang+end+period+food].append(int(infom[4]))

                        
    # 시간초과를 해결한 방법
    for key in info_dict.keys():
        info_dict[key].sort()
        
    for query in queries:
        query = query.replace(" and ", "")
        query = query.split()

        query_score = int(query[1])
        query = query[0]

        # 점수
        # info_score = info_dict[query]
        l = len(info_dict[query])
        tmp = l

        low, high = 0, l - 1

        while low <= high:
            mid = (low + high) // 2

            if query_score <= info_dict[query][mid]:
                tmp = mid
                high = mid - 1

            else:
                low = mid + 1

        answer.append(l - tmp)
    return answer