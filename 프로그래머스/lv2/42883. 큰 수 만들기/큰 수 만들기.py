def solution(number, k):

    count = 0
    i = 0
    stack = []

    while count != k:
        if i == len(number):
            stack.pop()
            count += 1
            continue

        if not stack:
            stack.append(int(number[i]))
            i += 1
            continue

        if int(number[i]) > stack[-1]:
            stack.pop()
            count += 1
        else:
            stack.append(int(number[i]))
            i += 1

    for res in range(i, len(number)):
        stack.append(int(number[res]))

    answer = "".join(list(map(str, stack)))
    return answer