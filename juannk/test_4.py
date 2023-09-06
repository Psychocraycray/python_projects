import math


def solution(x, a):
    total_sum = sum(a)
    abs_sum = abs(total_sum)
    min_steps = math.ceil(abs_sum / x)
    return min_steps


input_list = input().split()
n = int(input_list[0])
x = int(input_list[1])
a = list(map(int, input().split()))

print(solution(x, a))