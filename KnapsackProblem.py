"""
Implementing 0-1 knapsack problem
Two ways of representation has been depicted here
"""

"""
Naive recursive approach
Time complexity : 2^n
This approach has exponential time complexity as each subproblem
has to be evaluated twice. Although time complexity can be reduced
if we use memoisation for evaluate each recursive call
"""
def recursiveKnapsackWithNoMemoisation(w, wt, val, n):


    if n == 0 or w == 0:
        return 0

    if wt[n-1] > w:
        return recursiveKnapsackWithNoMemoisation(w, wt, val, n-1)
    else:
        return max(val[n-1] + recursiveKnapsackWithNoMemoisation(w - wt[n-1], wt, val, n-1), recursiveKnapsackWithNoMemoisation(w, wt, val, n-1))

"""
Iterative Approach
Time Complexity : O(nw)
"""
def iterativeKnapsack(w, wt, val, n):

    tempArr = [[0 for x in range(w+1)] for x in range(n+1)]

    for i in range(n+1):
        for weight in range(w+1):
            if i == 0 or weight == 0:
                tempArr[i][weight] = 0
            elif wt[i-1] <= weight:
                tempArr[i][weight] = max(val[i-1] + tempArr[i-1][weight - wt[i-1]], tempArr[i-1][weight])
            else:
                tempArr[i][weight] = tempArr[i-1][weight]

    return tempArr[n][w]

val = [1, 4, 5, 7]
wt = [1, 3, 4, 5]
maxWt = 7
n = len(wt)

print recursiveKnapsackWithNoMemoisation(maxWt, wt, val, n)

print "===="
print iterativeKnapsack(maxWt, wt, val, n)
