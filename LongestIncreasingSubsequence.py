"""
Implementing Longest Increasing Subsequence using
dynamic programming
"""

"""
Time Complexity : O(n^2)
Space Complexity : O(n)
"""
def lcs(arr):
    arrLen = len(arr)

    """
    Create a temporary array to store the maximum length of
    Longest Common subsequence
    """
    arrTemp = [1] * arrLen

    """
    iterating though the array and comparing each value with
    the values before the current index to check weather there
    exist value's which is less that the current value under
    consideration
    """
    for i in range(1, arrLen):
        """
        iterating through the array and comparing all the values with
        the values before the current index under consideration and
        incrementing the temporary array value for that index if the
        condition is met
        """
        for j in range(0, i):
            """
            if the value at i'th index is greater than value in arr at j'th index
            and value in temporary array at j'th index + 1 is greater than of value
            at i'th index of temporary array then increment the value in temporary
            array
            """
            if arr[i] > arr[j] and (arrTemp[j] + 1) > arrTemp[i]:
                arrTemp[i] = arrTemp[j] + 1

    maxi = 0
    """
    return the maximum value of temporary array as it will result
    in the value of longest common subsequence
    """
    for item in arrTemp:
        maxi = max(maxi, item)

    return maxi


arr = [10, 22, 9, 33, 21, 50, 41, 6]

# print the length of longest common subsequence
print lcs(arr)
