"""
You will be given a stream of numbers, one by one. After each new number,
return the median of the numbers so far.

we can use a max heap on the left side to represent elements that are less than effective median,
and a min-heap on the right side to represent elements that are greater than effective median.
time complexity O(n * log(n)), n refer to size of thearray
space complexity O(n), an extra heap of size n is needed
time spent on the question: about 40 min"""

import heapq


def runningMedian(arr):
    res = []
    g = []
    s = []
    for i in range(len(arr)):
        # Negation for treating it as max heap
        heapq.heappush(s, -arr[i])
        heapq.heappush(g, -heapq.heappop(s))
        if len(g) > len(s):
            heapq.heappush(s, -heapq.heappop(g))

        if len(g) != len(s):
            res.append([i + 1, -s[0]])
        else:
            res.append([i + 1, (g[0] - s[0]) / 2])
    return res


if __name__ == '__main__':
    arr1 = [1, 11, 4, 15, 12]
    print(runningMedian(arr1))
