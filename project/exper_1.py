while True:
    try:
        inp = int(input("please enter number of tuples: "))
        break
    except ValueError:
        print("invalid input please try a positive or negative integer")

for _ in range(inp):
    while True:
        try:
            n = int(input("how many integers do you want to input: "))
            a = list(map(int, input("please enter list of a's use ',' between each number: ").split(',')))
            b = list(map(int, input("please enter list of b's use ',' between each number: ").split(',')))
            break
        except ValueError:
            print("please try again with a positive or negative integer")

    tuples = [(a[i], b[i]) for i in range(n)]
    tuples_sorted = sorted(tuples, key=lambda x: (-abs(x[1])))

    max_score = float('-inf')

    for k in range(n):
        if (k == 4 and set([1, 2, 3, 4 ]).issubset(set(range(n)))) or (k == 3 and set([1, 2, 3]).issubset(set(range(n)))) or (k == 1 and set([2])):
            sum1 = sum(tuples[i][0] for i in range(k))
            sum2 = sum(tuples[i][0] for i in range(k))
            score = sum1 * sum2
            max_score = max(max_score, score)

    print(max_score)
6
2 2 2
1 1
1 2
2 2 2
1 1
2 2
2 2
1 2 1
1 1
1 2
5 5 4
3 3
1 1
1 5
5 1
5 5
2 2 2
1 1
2 1
1 2
3 4 1
1 2
3 3
