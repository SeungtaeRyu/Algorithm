from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []

    # 코스요리 개수 순회
    for n in course:
        count_list = []
        max_count = 0

        # 주문들 순회
        visited = defaultdict(int)
        for order in orders:
            # 각 주문당 코스요리 개수 조합 뽑기
            for johap in combinations(order, n):
                temp = "".join(sorted(johap))

                if visited[temp] == 1:
                    continue
                visited[temp] = 1

                count = 0
                for order2 in orders:
                    for menu in johap:
                        if menu not in order2:
                            break
                    else:
                        count += 1
                if count >= 2:
                    if count > max_count:
                        count_list = [temp]
                        max_count = count
                    elif count == max_count:
                        count_list.append(temp)

        for count_list_item in count_list:
            answer.append(count_list_item)

    answer.sort()

    return answer