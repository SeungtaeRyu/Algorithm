n = int(input())
decided = {chr(i): 0 for i in range(65, 91)}
for _ in range(n):
    word = input()
    for i in range(len(word)):
        decided[word[i]] += 10**(len(word)-1-i)
count_num = []
for i in range(65, 91):
    if decided[chr(i)] != 0:
        count_num.append(decided[chr(i)])
count_num.sort(reverse=True)
count = 9
total = 0
for i in range(len(count_num)):
    total += count_num[i] * count
    count -= 1
print(total)
