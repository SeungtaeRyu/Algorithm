word = list(input())

asci_code = [0] * 26
for value in word:
    asci_code[ord(value)-65] += 1

odd = 0
for count in asci_code:
    if count % 2:
        odd += 1

result = ''
if len(word) % 2:
    if odd <= 1:
        for i in range(26):
            for j in range(asci_code[i] // 2):
                result += chr(i+65)
        for i in range(26):
            if asci_code[i] % 2:
                result += chr(i+65)
        result += result[-2::-1]
        print(result)
    else:
        print("I'm Sorry Hansoo")
else:
    if odd == 0:
        for i in range(26):
            for j in range(asci_code[i] // 2):
                result += chr(i+65)
        result += result[::-1]
        print(result)
    else:
        print("I'm Sorry Hansoo")
