"""
The Catalan numbers are a mathematical sequence of numbers.
The nth Catalan number is defined as (2n)! / (n+1)!n!.
Given a non-negative integer n, return the Catalan numbers 0-n.
we use dynamic programming, dp[i] means the ith Catalan number, and
dp[i+1] = [(2n-1)(2n)/n(n+1)] * dp[i]
time complexity O(n), n refer to number
space complexity O(1), no extra space is needed
time spent on the question: about 15 min"""


def catalanNumbers(n):
    res = [1]
    if n == 0:
        return res
    for i in range(1, n + 1):
        cur = res[-1] * (2 * i - 1) * 2 // (i + 1)
        res.append(cur)
    return res


if __name__ == '__main__':
    print(catalanNumbers(1))
    print(catalanNumbers(5))
