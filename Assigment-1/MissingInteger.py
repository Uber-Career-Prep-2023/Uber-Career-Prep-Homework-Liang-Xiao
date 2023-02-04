# strategy: traverse the array, compare the element with the position
# conditions to make sure : n >= 1
# time complexity: O(n), n refer to the length of the input array
# space complexity O(1), an extra dictionary is added
# time to complete, roughly 10 minutes
def MissingInteger(arr, n):
    res = n
    for i in range(n - 1):
        if arr[i] != i + 1: # find the missing integer, and break the loop
            res = i + 1
            break
    return res


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 6, 7]
    n = 7
    print(MissingInteger(arr, n))
    arr = [1]
    n = 2
    print(MissingInteger(arr, n))
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]
    n = 12
    print(MissingInteger(arr, n))
