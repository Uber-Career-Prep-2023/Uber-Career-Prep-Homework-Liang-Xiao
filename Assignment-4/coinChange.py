"""
Given a list of coin denominations and a target sum,
return the number of possible ways to make change for that sum.


we use dynamic programming, dp[i] means number of possible ways to make change for i. we
want to compute dp[target]
we can loop through coins, for one coin, if we know dp[i - coin], we can add it to dp[i]

time complexity O(target*n), n refer to size of the coins
space complexity O(target), an extra array of size target is needed
time spent on the question: about 30 min
"""


def coinChange(coins, target):
    dp = [0 for i in range(target + 1)]
    dp[0] = 1  # no need to make changes
    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]
    return dp[target]


if __name__ == "__main__":
    coins = [2, 5, 10]
    target = 20
    print(coinChange(coins, target))
    target = 15
    print(coinChange(coins, target))
