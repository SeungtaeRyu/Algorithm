import sys
sys.stdin = open("input.txt", encoding='UTF8')


for tc in range(1, 11):
    _ = input()
    search = input()
    word = input()
    print(f'#{tc} {word.count(search)}')