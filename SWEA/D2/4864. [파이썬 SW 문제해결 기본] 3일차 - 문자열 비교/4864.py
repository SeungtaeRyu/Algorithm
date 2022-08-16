import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    a = input()
    b = input()

    c = b.replace(a,'')

    if len(b) == len(c):
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')