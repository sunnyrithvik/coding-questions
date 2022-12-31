import numpy as np

num = np.random.randint(1, 101, 10)
n = len(num)
print(num, min(num))

for j in range(n):
    mini = j
    for i in range(j+1, n):  # u can also use j instead of j+1
        if num[mini] > num[i]:
            mini = i
    num[j], num[mini] = num[mini], num[j]

print(num)
'''
Selection Sort Applications

The selection sort is used when
    # a small list is to be sorted
    # cost of swapping does not matter
    # checking of all the elements is compulsory
    # cost of writing to a memory matters like in flash memory 
    (number of writes/swaps is O(n) as compared to O(n2) of bubble sort)
'''