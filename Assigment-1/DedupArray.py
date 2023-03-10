"""# strategy: use sliding window technique to remove duplicate elements
as the array is already sorted, all the duplicate elements is continuous in the array
1. the left pointer and the right pointing begin with the second index of the array
2. loop through the array to check whether element at right pointer is a duplicate element
    if so, do nothing, if not, keep its value in the left pointer and move the left pointer by 1
3. delete all the elements from the left pointer to the end, these elements are duplicates

# conditions to make sure : arr is None or len(arr) <= 1

# time complexity: O(n), n refer to the length of arr

# space complexity O(1), constant space needed

# time to complete, roughly 15 minutes"""


def DedupArray(arr):
    if arr is None or len(arr) <= 1:
        return arr
    left = 1
    right = 1
    n = len(arr)

    # move right pointer to check elements in the array, when element at right pointer is not a duplicate element,
    # keep it in the left pointer, and move left pointer.
    # this method makes sure that all the elements before left pointer is unique.
    while right < n:
        if arr[left - 1] != arr[right]:  # element at right pointer is not a duplicate element
            arr[left] = arr[right]
            left += 1
        right += 1

    # delete all the elements from left pointer.
    while left < n:
        del arr[-1]
        left += 1


if __name__ == "__main__":
    arr_input = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    DedupArray(arr_input)
    print(arr_input)
    arr_input = [0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15]
    DedupArray(arr_input)
    print(arr_input)
    arr_input = [1, 3, 4, 8, 10, 12]
    DedupArray(arr_input)
    print(arr_input)
