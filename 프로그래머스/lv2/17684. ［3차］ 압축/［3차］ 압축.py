from collections import defaultdict

def solution(msg):
    answer = []
    d = defaultdict(int)
    num = 27
    
    for i in range(65, 91):
        d[chr(i)] = i-64
    
    index = 0
    
    while index < len(msg):
        word = ""
        maxWord = ""
        maxIndex = 0
        for i in range(index, len(msg)):
            word += msg[i]
            if d[word]:
                maxWord = word
                maxIndex = i

        answer.append(d[maxWord])

        index = maxIndex + 1
        if index != len(msg):
            d[maxWord+msg[index]] = num
            num += 1
    
    return answer