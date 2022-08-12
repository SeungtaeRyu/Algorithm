T = int(input())

for test_case in range(T):
    ps = list(input())
    vps = []
    complete_for = True
    for p in ps:
        if p == '(':
            vps.append(p)
        else:
            if len(vps) == 0:
                complete_for = False
                break
            else:
                vps.pop()
    if complete_for and len(vps) == 0:
        print("YES")
    else:
        print("NO")