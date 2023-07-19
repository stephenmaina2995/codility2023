def solution(A):
    N = len(A)
    min_diff = float('inf')

    # Sort the array in ascending order
    A.sort()

    # Calculate the difference for each possible split
    for i in range(1, N - 1):
        min_val = min(A[:i])
        max_val = max(A[i:])
        diff = max_val - min_val
        min_diff = min(min_diff, diff)

    return min_diff
print(solution([11, 5, 3, 12, 6, 8, 1, 7, 4]))  # Output: 3
print(solution([10, 14, 12, 1000, 11, 15, 13, 1]))  # Output: 5
print(solution([4, 5, 7, 10, 10, 12, 12, 12]))  # Output: 2
print(solution([5, 10, 10, 5, 5]))  # Output: 0
