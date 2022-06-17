"""
Q: Given an array of integers nums containing n + 1 integers where each integer is in the
 range [1, n] inclusive. There is only one repeated number in nums, return this repeated number.
Example:
I/P: nums = [1, 3, 4, 2, 2]
O/P: 2
"""

arr = [1, 3, 4, 2, 3]

# doubt

'''
def duplicatenumber(arr):
    arr.sort()
    n = len(arr)

    for i in range(n):
        if arr[i] == arr[i + 1]:
            return arr[i]


print(duplicatenumber(arr))
'''

# check this once not working as described
def duplicatenumber2(arr):
    ans = 0
    n = len(arr)
    for i in range(n):
        ind = abs(arr[i])
        if arr[ind-1] < 0:
            return abs(arr[i])
        else:
            arr[ind-i] = -1*arr[ind-1]
    return -1


print(duplicatenumber2(arr))
