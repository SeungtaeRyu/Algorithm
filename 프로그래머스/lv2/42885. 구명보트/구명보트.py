def solution(people, limit):
    answer = 0
    start = 0
    end = len(people)
    people.sort(reverse=True)
    while start < end:
        if limit - people[start] >= people[end-1]:
            end -= 1
        start += 1
        answer += 1
    return answer