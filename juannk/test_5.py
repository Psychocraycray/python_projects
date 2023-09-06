def calculate_editorial_duration(n, k, durations):
    min_duration = float('inf')

    for i in range(k + 1):
        mono_carp_duration = sum(durations[:i])
        poly_carp_duration = sum(durations[i:k])

        max_duration = max(mono_carp_duration, poly_carp_duration)
        min_duration = min(min_duration, max_duration)

    return min_duration


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    durations = list(map(int, input().split()))
    min_duration = calculate_editorial_duration(n, k, durations)
    print(min_duration)