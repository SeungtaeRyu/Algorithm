a, b, c = map(int, input().split())

list1 = [a,b,c]
temp = 0
i = 0

while i < 3:
    j = i + 1
    while j < 3:
        if list1[i] < list1[j]:
            temp = list1[i]
            list1[i] = list1[j]
            list1[j] = temp
        j += 1
    i += 1

print(list1[1])