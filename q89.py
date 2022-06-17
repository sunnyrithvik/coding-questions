"""
Q: Given two strings a and b. Check if the string 'b' can be obtained by rotating another string 'a' by
 exactly 2 places.
Example:
I/P: a = "amazon", b= "azonam"
O/P: 1
* amazon can be rotated anti clockwise by two places, which will make it as azonam.
"""

s1 = 'amazon'
s2 = 'azonam'


def isrotated(s1, s2):
    if len(s1) != len(s2):
        return False

    n = len(s1)
    flag1 = True
    flag2 = True

    ''' here one is clockwise and another anticlockwise '''
    for i in range(n):
        if s1[i] != s2[(i + 2) % n]:
            flag1 = False
        if s1[i] != s2[(n - 2 + i) % n]:
            flag1 = False

    return flag1 | flag2


print(isrotated(s1, s2))
