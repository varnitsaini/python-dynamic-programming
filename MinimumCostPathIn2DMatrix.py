"""
Illustrating Minimum Cost Path in 2D n*n matrix. Given Constraint
is that you can only move in either right or downward direction
The logic behind solving such kind of problems are:
- Optimal Sub-structure
- Overlapping Sub-Problems
"""

def minCostPath(arr):

    """
    We initialise a temporary array where we will store the minimum distance
    of every previous node discovered either from the node to the left or
    node above of it
    """
    tempArr = [[0 for i in range(len(arr))] for j in range(len(arr))]

    """
    Assign first value of the array into the temporary array
    """
    tempArr[0][0] = arr[0][0]

    """
    Handling the base cases for the first row of the temporary array
    """
    for i in range(1, len(arr)):
        tempArr[0][i] = tempArr[0][i-1] + arr[0][i]

    """
    Handling the base cases for the first column of the temporary array
    """
    for j in range(1, len(arr)):
        tempArr[j][0] = tempArr[j-1][0] + arr[j][0]

    """
    Finding the minimum value for the temporary array to build temporary array
    from adjacent left node or node above of it
    """
    for i in range(1, len(arr)):
        for j in range(1, len(arr)):
            tempArr[i][j] = min(tempArr[i-1][j], tempArr[i][j-1]) + arr[i][j]

    """
    Returning minimum distance of the last index of the the array ie value of
    last row and last column
    """
    return tempArr[i][j]


arr = [[2, 1, 5]
      ,[10, 3, 6]
      ,[7, 4, 8]]

"""
Print the minimum cost
"""
print minCostPath(arr)