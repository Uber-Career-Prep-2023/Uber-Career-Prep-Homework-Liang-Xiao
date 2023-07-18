"""
you can only climb one or two stairs at once.
 Given an array representing the costs per stair,
what is the minimum possible toll you can pay to climb the staircase?

we can use dynamic programming, dp[i] meaning the min cost to reach ith staircase from start.
dp[i] = min(dp[i-1],dp[i-2]) + cost[i]
time complexity O(n), n refer to size of the array
space complexity O(1), no extra space is needed
time spent on the question: about 15 min"""


def MinCostStairClimbing(cost):
    if len(cost) <= 1:
        return 0
    step1 = cost[0]
    step2 = cost[1]
    for i in range(2, len(cost)):
        cur = min(step1, step2) + cost[i]
        step1 = step2
        step2 = cur
    return min(step1, step2)


if __name__ == '__main__':
    arr = [4, 1, 6, 3, 5, 8]
    print(MinCostStairClimbing(arr))
    arr = [11, 8, 3, 4, 9, 13, 10]
    print(MinCostStairClimbing(arr))
