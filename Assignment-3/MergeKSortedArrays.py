"""
Given an array of k sorted arrays, merge the k arrays into a single sorted array.

time complexity O(n * log(k)), n refer to size of the merged array
space complexity O(k), an extra heap of size k is needed
time spent on the question: about 15 min
"""
import heapq


def MergeKSortedArrays(k, arrays):
    min_list = [(arrays[i][0], i, 0) for i in range(k)]  # collect the first elements of arrays
    heapq.heapify(min_list)  # build a heap to extract the min element easily

    merged_array = []
    # calculate the size of the merged array
    size = 0
    for i in range(k):
        size += len(arrays[i])

    # fill the merged array using heap
    while len(merged_array) < size:
        # extract the min element from the heap
        min_num, i, j = heapq.heappop(min_list)
        # add new element to the heap
        if j < len(arrays[i]) - 1:
            j += 1
            heapq.heappush(min_list, (arrays[i][j], i, j))
        # fill the merged array with the min element
        merged_array.append(min_num)

    return merged_array


if __name__ == "__main__":
    input_arr = [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]
    print(MergeKSortedArrays(2, input_arr))
    input_arr = [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]
    print(MergeKSortedArrays(3, input_arr))
