'''
Q: Given an array Arr[] that contains N integers. Find
the product of the maximum product subarray.
Example:
I/P: n=5, arr[] = {6, -3, -10, 0,2}
O/P: 180
* Subarray with maximum product is [6, -3, -10] which gives product as 180.
'''

n = 5
arr = [6, -3, -10, 0, 2]


def maxproduct(arr, n):
    ans = minm = maxm = arr[0]

    for i in range(1, n):
        curr = arr[i]
        if curr < 0:
            maxm, minm = minm, maxm

        maxm = max(curr, maxm * curr)
        minm = min(curr, minm * curr)

        ans = max(ans, maxm)

    print(ans)


maxproduct(arr, n)
