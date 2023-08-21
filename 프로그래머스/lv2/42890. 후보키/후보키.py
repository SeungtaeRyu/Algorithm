from itertools import combinations

def solution(relation):
    answer = []
    column = [i for i in range(len(relation[0]))]

    # 단일 항목 유일성 검사
    for c in column:
        temp = set()
        for row in relation:
            temp.add(row[c])
        if len(temp) == len(relation):
            answer.append([c])

    # 단일 항목 유일성 통과 항목 제외
    # for ans in answer:
    #     column.pop(ans[0])

    # 2개 이상 조합
    results = []
    for r in range(2, len(column) + 1):  # 2개부터 리스트의 길이까지의 모든 조합을 구합니다.
        results.extend(combinations(column, r))

    # 2개 이상 조합에서 검증
    for result in results:
        # 최소성 검사
        # flag = True
        for ans in answer:
            for a in ans:
                if a not in result:
                    break
            else:
                # 유일성을 가진 속성이 모두 포함된 조합일 때
                break
        else:
            # 상위 else문의 브레이크에 걸리지 않으면 유일성 검사
            temp = set()
            for row in relation:
                str = ""
                for r in result:
                    str += row[r]
                temp.add(str)
            if len(temp) == len(relation):
                answer.append(list(result))

    return len(answer)