t = int(input())
for i in range(t):
    n, k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    a.sort()
    remaining_ops = k
    i = 0
    j = n - 1
    while remaining_ops > 0 and i < j:
        if a[i] + a[i+1] < a[j]:
            a.pop(i)
            a.pop(i)
            j -= 2
            remaining_ops -= 1
        else:
            a.pop(j)
            i += 1
            j -= 1
            remaining_ops -= 1
    print(sum(a))
