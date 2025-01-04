# In the popular game of Bingo, a player has a card represented by a matrix mat of size n x m that contains all numbers from the range 1 to n x m.
# The numbers are called out from an array arr of all the numbers from 1 to n x m in sequential order starting from the first element.
# When a number is called out, the player marks the corresponding number on the game card.
# Find the first number in the sequence at which either a row or a column is completely marked

# Example
# Let mat=[[3,1,8],[4,6,2],[7,5,9]] and arr=[5,4,8,7,6,1,9,2,3]
# The 2nd column is completely marked after 1 is called Return 1

# Function Description
# Complete the function getBingoChallenge below 
# getBingoChallenge has the following parameter(s):
# int mat[n][m]: the bingo card
# int arr[n*m]: the numbers in the order they are called out

# Returns
# int: the first number  at which either a row or a column is completely marked


# Solution
def getBingoChallenge(mat, arr):
    n = len(mat)
    m = len(mat[0])
    rows = [0]*n
    cols = [0]*m
    for i in range(n):
        for j in range(m):
            if mat[i][j] in arr:
                rows[i] += 1
                cols[j] += 1
                if rows[i] == m or cols[j] == n:
                    return mat[i][j]
    return -1