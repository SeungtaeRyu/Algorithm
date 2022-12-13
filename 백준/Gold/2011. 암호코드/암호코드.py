dp = [0 for _ in range(5001)]
dp[0] = 1
dp[1] = 1

for i in range(2,5001):
    dp[i] = (dp[i-1]+dp[i-2]) % 1000000

nums = input().rstrip()
nums = nums.replace('10', 'x')
nums = nums.replace('20', 'x')
nums = list(nums)

isTwo = []

if not nums:
    print(0)
    exit()

# 유효성 검사
for i in range(len(nums)):
    if nums[i] == '0':
        print(0)
        exit()

for i in range(1, len(nums)):
    if nums[i] == 'x' or nums[i-1] == 'x':
        isTwo.append(1)
    else:
        temp = nums[i-1]+nums[i]
        if int(temp) <= 26:
            isTwo.append(2)
        else:
            isTwo.append(1)
isTwo.append(1)

total = 1
index = 0
while index < len(isTwo):
    count = 1
    while isTwo[index] == 2:
        count += 1
        index += 1
    total = (total * dp[count]) % 1000000
    index += 1
print(total)
