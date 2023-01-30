a = int(input())
n = int(input())
ans = 0
for i in range(n):
    b, c = map(int, input().split())
    ans += b*c
if a == ans:
    print("Yes")
else:
    print("No")