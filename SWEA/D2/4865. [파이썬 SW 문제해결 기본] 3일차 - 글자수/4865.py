import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    str1 = set(list(input()))
    str2 = list(input())

    count = 0
    for value in str1:
        count = max(count, str2.count(value))

    print(f'#{tc} {count}')