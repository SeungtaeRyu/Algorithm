n = input()

a = list(n.split("0"))
b = list(n.split("1"))

a_count = 0
for i in range(len(a)):
    if a[i] != '':
        a_count += 1
b_count = 0
for i in range(len(b)):
    if b[i] != '':
        b_count += 1

print(min(a_count, b_count))