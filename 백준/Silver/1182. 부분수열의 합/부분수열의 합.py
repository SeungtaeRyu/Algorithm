def f(i, N, t, s):
    global answer
    if i == N:
        if t == s:
            answer += 1
        return
    # elif t > s:
    #     return
    else:
        f(i+1, N, t + numbers[i], s)
        f(i+1, N, t, s)

n, s = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort()

answer = 0
f(0, n, 0, s)
if s == 0:
    answer -= 1
print(answer)