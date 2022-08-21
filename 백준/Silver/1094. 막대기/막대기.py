num = int(input())

count = 0
while num != 0:
    temp = 1
    while temp <= num:
        temp *= 2       # 1 2 4 8 16 32 64
    temp //= 2          # 32
    num -= temp
    count += 1
print(count)