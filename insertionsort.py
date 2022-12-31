import numpy as np

num = np.random.randint(1, 101, 10)
n = len(num)
print(num, min(num), max(num))

for i in range(1, n):  # u can use range(n) instead of range(1,n)
    k = num[i]
    j = i-1

    while j >= 0 and k < num[j]:
        num[j+1] = num[j]
        j = j-1
    num[j+1] = k

print(num)
'''
Insertion Sort Applications

The insertion sort is used when:
    # the array is has a small number of elements
    # there are only a few elements left to be sorted
'''