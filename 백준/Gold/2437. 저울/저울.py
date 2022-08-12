num = int(input())
weights = list(map(int, input().split()))

weights.sort()


if weights[0] != 1:
    print('1')
else:
    cumulative_sum = 0
    for i in range(len(weights)):
        cumulative_sum += weights[i]
        if i == len(weights) - 1 :
            print(cumulative_sum+1)
            break

        if cumulative_sum + 1 < weights[i+1]:
            print(cumulative_sum+1)
            break

