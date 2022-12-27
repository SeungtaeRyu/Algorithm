nums = list(map(int, list(input())))

x = 0
y = 0
temp = 2**(len(nums))
for i in range(len(nums)):
    temp //= 2
    if nums[i] == 0:
        continue
    elif nums[i] == 1:
        x += temp
    elif nums[i] == 2:
        y += temp
    elif nums[i] == 3:
        x += temp
        y += temp
print(len(nums), x, y)