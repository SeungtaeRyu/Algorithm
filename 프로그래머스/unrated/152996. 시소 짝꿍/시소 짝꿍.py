from collections import defaultdict

def solution(weights):
    answer = 0
    count = defaultdict(int)

    for w in weights:
        answer += count[w] + count[(w * 2) / 3] + count[(w * 3) / 2] + count[w * 2] + count[w / 2] + count[(w * 3) / 4] + count[(w * 4) / 3]
        count[w] += 1

    return answer

print(solution([100,180,360,100,270]))