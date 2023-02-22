"""
# strategy: use a dictionary to store the count of num in the arr
1. create a dictionary to store the count of num in the arr
2. loop through the array, for current number x, add the count of number equals to k - x,
    as this is the number of pairs that sum to k.
3. in the same loop, update the count of the current number x in the dictionary

# conditions to make sure : arr is  None or len(arr) <= 1

# time complexity: O(n), n refer to the length of arr

# space complexity O(n), an extra dictionary is needed, n refer to the length of arr

# time to complete, roughly 20 minutes"""

from collections import defaultdict


def TwoSum(arr, k):
    if arr is None or len(arr) <= 1:
        return 0
    dict_element = defaultdict(int)
    res = 0
    for num in arr:
        res += dict_element[k - num]  # add the count of number equals to k - num
        dict_element[num] += 1  # update the count of the current number
    return res


if __name__ == "__main__":
    arr_input = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
    print(TwoSum(arr_input, 10))
    print(TwoSum(arr_input, 8))
    arr_input = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
    print(TwoSum(arr_input, 6))
    print(TwoSum(arr_input, 1))
