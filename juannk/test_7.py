def sol_n(a):
    count = 0
    for i in range(len(a) - 2, -2, -1):
        if sorted(a[i + 1:]) != a[i + 1:]:
            return max(a[:i + 2])
    return count


cases = int(input())
for _ in range(cases):
    _ = input()  # Discard the input length as it is not used
    a = list(map(int, input().split()))
    print(sol_n(a))
