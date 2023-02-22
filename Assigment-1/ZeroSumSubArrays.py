"""
# strategy: using a dictionary to store the count of the sum of the elements [0:i].
 1. create a dictionary to store the count of the sum of the elements [0:i].
 2. loop through the array and calculate the sum of array[0:i]
 3. check if sum of array[0:i] exist in the dictionary.
     if so, it means there exists j such that sum of array[0:i] = sum of array[0:j] (j < i), meaning sum of array[i:j] = 0.
     add all existing subarray such that sum of array[i:j] = 0 to the result.
 4. update the dictionary after checking

# base cases : input is none or empty array, just return 0

# time complexity: O(n), n refer to the length of the input array

# space complexity O(n), a dictionary is added to store the count of the sum of the elements [0:i].

# time to complete, roughly 40 minutes. it takes longer reasoning out the solution"""


def ZeroSumSubArrays(arr):
    count = 0
    sum_num = 0
    dict_sums = {0: 1}  # put 0 in the dictionary first
    for i in range(len(arr)):
        sum_num += arr[i]  # calculate the sum of array[0:i]
        if sum_num in dict_sums:  # sum of array[0:i] = sum of array[0:j] (j < i), meaning sum of array[i:j] = 0.
            count += dict_sums[sum_num]  # add all existing subarray such that sum of array[i:j] = 0.
            dict_sums[sum_num] += 1  # put sum of array[0:i] in the dictionary
        else:
            dict_sums[sum_num] = 1  # put sum of array[0:i] in the dictionary
    return count


if __name__ == "__main__":
    arr1 = [4, 5, 2, -1, -3, -3, 4, 6, -7]
    arr2 = [1, 8, 7, 3, 11, 9]
    arr3 = [8, -5, 0, -2, 3, -4]
    print(ZeroSumSubArrays(arr1))
    print(ZeroSumSubArrays(arr2))
    print(ZeroSumSubArrays(arr3))
