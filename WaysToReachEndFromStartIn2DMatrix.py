"""
Illustrating number of ways to reach to the end of 2D matrix
Starting from the beginning ie from index (0,0) to (m, n)
where m is number of rows and n is number of columns.
The constraint here is that you can either move in downward
direction or you can move to right direction but not diagonally
"""

def numWaysToEnd(m, n, dict):

    """
    Base condition for recursion ie if m equal to one or n equal to one then
    return one because after that there will be only one way to reach the origin
    """
    if m == 1 or n == 1:
        return 1

    """
    make a temporary dict variable and check if the temp variable exist in our dict
    if it exist then return the value as it is and if it doesnt exist then calculate
    the recursive value to find the number of the ways to reach to the origin ie
    node (0, 0) from node (m, n)
    """
    tempDictStr = str(m) + "-" + str(n)
    if tempDictStr in dict:
        return dict[tempDictStr]
    else:
        dict[tempDictStr] = numWaysToEnd(m-1, n, dict) + numWaysToEnd(m, n-1, dict)
        return dict[tempDictStr]

dict = {}
m = 20
n = 20

"""
print number of ways to reach to the end of the matrix from the
origin of the matrix
"""
print numWaysToEnd(m, n, dict)

