import numpy as np
num = np.random.randint(1, 101, 10)
n = len(num)
'''
# 1st solution
for i in range(n):
    for j in range(n-1):
        if num[j] > num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]
print(n, num)

# 2nd solution
for i in range(n):
    for j in range(n-i-1):  # u can use range(n-1-i) (because already last i items are sorted)
        if num[j] > num[j + 1]:
            num[j], num[j + 1] = num[j + 1], num[j]
print(n, num)

# 3rd solution optimized bubble sort
for i in range(n):
    swapped = False
    for j in range(n-i-1):  # u can use range(n-1) (because already last i items are sorted)
        if num[j] > num[j + 1]:
            num[j], num[j + 1] = num[j + 1], num[j]
            swapped = True
        if not swapped:
            break
print(n, num)
'''