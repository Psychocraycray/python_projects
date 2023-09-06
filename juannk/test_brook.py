def solution(a: list[int]):
    smallest_gap = a[1] - a[0]

    # loop to get the smallest number
    for i in range(1, len(a) - 1):
        if smallest_gap > a[i + 1] - a[i]:
            smallest_gap = a[i + 1] - a[i]

    if smallest_gap % 2 == 1:
        # if smallest_gap is odd
        return int((smallest_gap + 1) / 2)
    else:
        return int(smallest_gap / 2) + 1


cases = int(input())
for i in range(cases):
    k = int(input())
    # we don't need k
    a = [int(x) for x in input().split(" ")]

    if a != sorted(a):
        # filters unsorted array
        print("results:", 0)
    else:
        print("results:", solution(a))
