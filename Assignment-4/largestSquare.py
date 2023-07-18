"""
Given a square matrix of 0s and 1s, 
find the dimension of the largest square consisting only of 1s.


we use dynamic programming, dp[i][j] means the largest dimension of 1s ending at (i,j)
at the right bottom corner. we have dp[i][j] = min(dp[i-1][j], dp[i][j-1],dp[i-1][j-1]) + 1 if
matrix[i][j] = 1

time complexity O(m*n), m,n refer to size of the matrix
space complexity O(m*n), an extra matrix of m*n is needed
time spent on the question: about 30 min"""


def largestSquare(matrix):
    m = len(matrix)
    n = len(matrix[0])
    dp = [[matrix[i][j] for i in range(n)] for j in range(n)]
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 1:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
    return dp[-1][-1]


if __name__ == "__main__":
    matrix1 = [[0, 1, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1], [0, 0, 1, 1]]
    print(largestSquare(matrix1))
