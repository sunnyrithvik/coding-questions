'''
Q: Given two arrays a[] and b[] of size n and m. Find the count of union elements of the two arrays.
Example:
I/P: n = 5, a[] = {1, 2, 3, 4,5}
     n = 3, b[] = {1, 2, 3}
O/P: 5
* 1, 2, 3, 4, 5 are the elements which comes in the union set of both arrays. So count is 5.
'''
n1 = 5
arr1 = [1, 10, 4, 5, 7]

n2 = 3
arr2 = [1, 2, 3]

arr = []


def twounion(n1, n2, arr1, arr2):
    for i in range(0, n1):
        arr.append(arr1[i])
    for j in range(0, n2):
        arr.append(arr2[j])

    print((set(arr)))
    print(len(set(arr)))


twounion(n1,n2,arr1,arr2)