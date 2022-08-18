import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    word = list(input())
    while len(word):
        for i in range(len(word)-1):
            if word[i] == word[i+1]:
                word.pop(i)
                word.pop(i)
                break
        else:
            print(f'#{tc} {len(word)}')
            break
