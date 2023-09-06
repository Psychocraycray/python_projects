import timeit
execution_time = timeit.timeit(stmt="""
case = int(input())


def try_shit(target_sum, result, all_results):
    for num1 in range(1, target_sum):
        num2 = 2 * num1
        if num1 + num2 == target_sum:
            result = [num1, num2]
            try_shit(num1, [], all_results)
            try_shit(num2, [], all_results)
            all_results.append(result)


for _ in range(case):
    target_sum, m = [int(i) for i in input().split()]
    result = []
    all_results = []

    try_shit(target_sum, result, all_results)

    #print(all_results)

    if target_sum == m or any(m in sublist for sublist in all_results):
        print("YES")
    else:
        print("NO")

""", number=1)
print(execution_time)
