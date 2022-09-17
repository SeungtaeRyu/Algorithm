n = int(input())

if n == 1:
    print(0)
else:
    nums = [False] * (n+1)

    for i in range(2, n+1):
        k = 2*i
        while k <= n:
            if nums[k]:
                k += i
                continue
            nums[k] = True
            k += i

    prime = []
    for i in range(2, n+1):
        if not nums[i]:
            prime.append(i)

    total = prime[0]
    s = 0
    e = 0
    count = 0
    # print(prime)
    while s < len(prime):
        # print(f's={s} e={e} total={total}')
        if total < n:
            if e < len(prime)-1:
                while e < len(prime)-1 and total < n:
                    e += 1
                    total += prime[e]
            else:
                total -= prime[s]
                if total == n:
                    count += 1
                s += 1
        else:
            if total == n:
                count += 1
            total -= prime[s]
            s += 1
    print(count)