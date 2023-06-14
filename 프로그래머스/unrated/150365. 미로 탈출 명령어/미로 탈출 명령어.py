def solution(n, m, x, y, r, c, k):
    global answer
    answer = ''
    count = abs(x-r) + abs(y-c)
    if k >= count and (k%2 == count%2):
        # 사전순 d > l > r > u
        direction = {'d': 0, 'l': 0, 'r': 0, 'u': 0}
        if x > r:
            direction['u'] += x - r
            k -= direction['u']
        else:
            direction['d'] += r - x
            k -= direction['d']
        if y > c:
            direction['l'] += y - c
            k -= direction['l']
        else:
            direction['r'] += c - y
            k -= direction['r']
        answer += 'd'*direction['d']
        d = min(int(k / 2), n - (x + direction['d']))
        answer += 'd' * d
        direction['u'] += d
        k -= 2 * d

        answer += 'l' * direction['l']
        l = min(int(k / 2), y - direction['l'] - 1)
        answer += 'l' * l
        direction['r'] += l
        k -= 2 * l

        answer += 'rl' * int(k / 2)
        answer += 'r' * direction['r']
        answer += 'u' * direction['u']

    else:
        answer = "impossible"
    return answer
