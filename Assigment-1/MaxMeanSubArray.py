"""
# strategy: using fixed-size sliding window,
 1. calculate the sum of the first k elements,
 2. iterate the array by adding one element from the right and removing one from the left to maintain k elements
     in the window
 3. update the max sum of the k elements with the larger sum.
 4. calculate the max mean k elements using max sum.

# questions to make sure: k >= 1 and len(arr) >= k

# time complexity: O(n), n refer to the length of the input array

# space complexity O(1), only constant extra space added

# time to complete, roughly 30 minutes"""


def MaxMeanSubArray(arr, k):
    sum_temp = sum(arr[0:k])  # calculate the sum of the first k elements
    index_start = 0
    index_end = k
    sum_max = sum_temp
    while index_end < len(arr):
        sum_temp = sum_temp - arr[index_start] + arr[index_end]  # calculate the sum of the next k elements
        sum_max = max(sum_temp, sum_max)  # update the max sum of the k elements with larger sum.
        index_start += 1
        index_end += 1
    return sum_max / k


if __name__ == '__main__':
    arr1 = [4, 5, -3, 2, 6, 1]
    arr2 = [1, 1, 1, 1, -1, -1, 2, -1, -1]
    arr3 = [1, 1, 1, 1, -1, -1, 2, -1, -1, 6]
    print(MaxMeanSubArray(arr1, 2))
    print(MaxMeanSubArray(arr1, 3))
    print(MaxMeanSubArray(arr2, 3))
    print(MaxMeanSubArray(arr3, 5))
