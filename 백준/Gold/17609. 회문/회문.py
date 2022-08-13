T = int(input())
for tc in range(1, T+1):
    word = input()
    word_1 = ''
    word_2 = ''
    for i in range(len(word)//2):
        if word[i] == word[-(1+i)]:
            continue
        else:
            word_1 = word[i:len(word)-1-i]
            word_2 = word[i+1:len(word)-i]
            break
    else:
        print(0)
        continue

    for i in range(len(word_1) // 2):
        if word_1[i] != word_1[-(1 + i)]:
            break
    else:
        print(1)
        continue

    for i in range(len(word_2) // 2):
        if word_2[i] != word_2[-(1 + i)]:
            break
    else:
        print(1)
        continue

    print(2)