import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    _, pw = input().split()
    result = []
    for i in pw:
        if not result:
            result.append(i)
        else:
            if result[-1] == i:
                result.pop()
            else:
                result.append(i)
    print(f'#{tc} {"".join(result)}')