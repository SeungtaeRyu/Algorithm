import sys
input = sys.stdin.readline

def sol():
    n = int(input())
    db = [input().strip() for _ in range(n)]
    db.sort()
    for j in range(n-1):
        if db[j] == db[j+1][:len(db[j])]:
            return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    print(sol())