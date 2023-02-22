"""
# strategy: traverse the array, compare the element with its index.
the elements are already sorted and has n - 1 elements containing all but one of the integers in the range 1-n
if the element is not missing, there should be n element and arr[i] = i + 1
loop through the array and check if arr[i] = i + 1, if not, i + 1 must be the missing element

# conditions to make sure : n >= 1

# time complexity: O(n), n refer to the length of the input array

# space complexity O(1), no extra space is added

# time to complete, roughly 10 minutes"""


def MissingInteger(arr, n):
    res = n
    for i in range(n - 1):
        if arr[i] != i + 1:  # find the missing integer, and break the loop
            res = i + 1
            break
    return res


if __name__ == "__main__":
    arr_input = [1, 2, 3, 4, 6, 7]
    print(MissingInteger(arr_input, 7))
    arr_input = [1]
    print(MissingInteger(arr_input, 2))
    arr_input = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]
    print(MissingInteger(arr_input, 12))
