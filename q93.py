# i = 0
# sum = 0
import numpy as np


ans=[]
N =3
arr=[5,2, 3]


def helper(arr, N, i=0, sum=0):
    if(i==N):
        ans.append(sum)
        return ans
    
    helper(arr, N, i+1, sum)
    helper(arr, N, i+1, sum + arr[i])
    return ans


def subsetSums(arr, N):
    helper(arr, N)
    return ans


ss = np.array(subsetSums(arr, N))
print(np.unique(ss))
