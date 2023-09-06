a, b = 0, 0


def arr(a, b):
    if a < b:
        return []
    if a % 3:
        return [a]
    return arr(a / 3, b) + arr((a / 3) * 2, b)


k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    if a == b or b in arr(a, b):
        print("YES")
    else:
        print("NO")
