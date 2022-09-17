def f(i, s_count, c_count, v_count, t):
    if s_count == l:
        if v_count >= 1 and c_count >= 2:
            ans.append(list(t))
            return
        else:
            return
    if i == c:
        return
    else:
        if word[i] in vowel:
            f(i+1, s_count+1, c_count, v_count +1, t+word[i])
            f(i+1, s_count, c_count, v_count, t)
        else:
            f(i+1, s_count+1, c_count+1, v_count, t+word[i])
            f(i+1, s_count, c_count, v_count, t)

l, c = map(int, input().split())
word = list(input().split())
ans = []
vowel = ['a', 'e', 'i', 'o', 'u']
f(0, 0, 0, 0, '')

for i in range(len(ans)):
    ans[i].sort()
ans.sort()

for i in ans:
    print(''.join(i))