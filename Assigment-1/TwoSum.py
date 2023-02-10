# strategy: use a dictionary to store the position list of num in the arr
# conditions to make sure : arr is  None or len(arr) <= 1
# time complexity: O(n), n refer to the length of arr
# space complexity O(n), an extra dictionary is needed, n refer to the length of arr
# time to complete, roughly 20 minutes

from collections import defaultdict


def TwoSum(arr, k):
    if arr is None or len(arr) <= 1:
        return 0
    dict_element = defaultdict(list)
    res = 0
    for i in range(len(arr)):
        val = dict_element[k - arr[i]]
        if len(val) > 0:  # find the pairs that sum to k
            res += len(val)  # each index in the list is unique
        dict_element[arr[i]].append(i)
    return res


if __name__ == "__main__":
    arr_input = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
    print(TwoSum(arr_input, 10))
    print(TwoSum(arr_input, 8))
    arr_input = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
    print(TwoSum(arr_input, 6))
    print(TwoSum(arr_input, 1))
