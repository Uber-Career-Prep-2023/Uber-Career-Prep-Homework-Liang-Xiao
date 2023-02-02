# strategy: using a set to store the prefix sum of the array
# base cases : input is none or empty array, just return 0
# time complexity: O(n), n refer to the length of the input array
# space complexity O(n), a set added to store the prefix sum of the array
# time to complete, roughly 40 minutes. it takes longer reasoning out the solution
def ZeroSumSubArrays(arr):
    count = 0
    sum_num = 0
    set_sums = set()
    set_sums.add(0)
    for num in arr:
        sum_num += num
        if sum_num in set_sums: # if sum_num exists, there exists a zero sum subarray
            count += 1
        else:
            set_sums.add(sum_num)
    return count


if __name__ == "__main__":
    arr1 = [4, 5, 2, -1, -3, -3, 4, 6, -7]
    arr2 = [1, 8, 7, 3, 11, 9]
    arr3 = [8, -5, 0, -2, 3, -4]
    arr4 = []
    print(ZeroSumSubArrays(arr1))
    print(ZeroSumSubArrays(arr2))
    print(ZeroSumSubArrays(arr3))
    print(ZeroSumSubArrays(arr4))
