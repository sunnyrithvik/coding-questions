"""
Q: Given an array A of n positive numbers. Find the first Equilibium Point in the array.
* Equilibrium Point in an array is a position such that the sum of elements before it
is equal to the sum of elements after it.
* Return -1 if no such point exists.
Example:
I/P: n=5, A[] = {1, 3, 5, 2, 2}
O/P: 3
"""

n = 5
arr = [1, 3, 5, 2, 2]


def equilibriumpoint(arr, n):
    totalsum = 0
    currentsum = 0

    for i in range(n):
        totalsum += arr[i]

    for i in range(n):
        totalsum = totalsum - arr[i]
        if currentsum == totalsum:
            return i + 1
        currentsum += arr[i]

    return -1


print(equilibriumpoint(arr, n))

