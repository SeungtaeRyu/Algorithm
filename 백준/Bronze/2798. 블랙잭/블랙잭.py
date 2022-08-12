n, m = map(int, input().split())

numbers = list(map(int, input().split()))

answer = 0
for i in range(n): 
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum = 0
            sum = numbers[i] + numbers[j] + numbers[k]
            if sum > m:
                continue
            else:
                if sum > answer:
                    answer = sum

print(answer)