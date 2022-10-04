import sys
input = sys.stdin.readline

n = int(input())

list2 = []
for i in range(1, n+1):
    a = n
    b = i
    list1 = []
    while a >= 0:
        list1.append(a)
        temp = a
        a = b
        b = temp - a

    list2.append(list1)

list2.sort(key= lambda x: -len(x))

print(len(list2[0]))
print(*list2[0])
