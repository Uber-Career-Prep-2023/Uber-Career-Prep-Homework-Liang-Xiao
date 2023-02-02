# strategy: using fixed-size sliding window
# questions to make sure: k >= 1 and len(arr) >= k
# time complexity: O(n), n refer to the length of the input array
# space complexity O(1), only constant extra space added
# time to complete, roughly 30 minutes

def MaxMeanSubArray(arr, k):
    sum_temp = sum(arr[0:k])
    index_start = 0
    index_end = k - 1
    sum_max = sum_temp
    while index_end < len(arr) - 1:
        sum_temp = sum_temp - arr[index_start] + arr[index_end + 1]
        sum_max = max(sum_temp, sum_max)
        index_start += 1
        index_end += 1
    return sum_max/k


if __name__ == '__main__':
    arr1 = [4, 5, -3, 2, 6, 1]
    arr2 = [1, 1, 1, 1, -1, -1, 2, -1, -1, 6]
    print(MaxMeanSubArray(arr1, 2))
    print(MaxMeanSubArray(arr1, 3))
    print(MaxMeanSubArray(arr2, 3))
    print(MaxMeanSubArray(arr2, 4))

