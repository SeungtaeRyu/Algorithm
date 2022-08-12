list1 = []

for i in range(8):
    list1.append(int(input()))
    
list2 = sorted(list1,reverse=True)

index_list = []
sum = 0
for i in range(5):
    sum += list2[i]
    index_list.append(list1.index(list2[i]))

index_list.sort()

result_list = []
for i in range(5):
    result_list.append(str(index_list[i]+1))

result = ' '.join(result_list)
print(sum)
print(result)
