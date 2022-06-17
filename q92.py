'''
Q: Given a mx n grid, count all the possible paths from top left to bottom right corner of the grid.
* From each cell you can either move to right or down.
* Top left corner (grid[0][0]), bottom right corner (grid[m - 1] [n - 1])
Example:
I/P: M = 3 and N = 3
O/P: 6
'''

m = n = 3


def countpath(i, j, m, n):
    if (i == m-1)|(j == n-1):
        return 1
    if (i >= m) | (j >= n):
        return 0
    a = countpath(i+1, j, m, n)
    b = countpath(i, j+1, m, n)

    return a+b


def numofpaths(m, n):
    return countpath(0,0, m, n)


print(numofpaths(m, n))
