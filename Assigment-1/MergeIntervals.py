# strategy: sort the interval by the low end and use a stack to store the intervals
# conditions to make sure : list_pairs is None or len(list_pairs) == 0
# time complexity: O(n), n refer to the length of list_pairs
# space complexity O(n), an extra deque is added, n refer to the length of list_pairs
# time to complete, roughly 35 minutes, longer to think of the stack technique
from collections import deque


def MergeIntervals(list_pairs):
    if list_pairs is None or len(list_pairs) == 0:
        return list_pairs

    def keyFun(input_list):
        return input_list[0]

    result = []
    list_pairs.sort(key=keyFun)  # sort the interval by the low end
    stack = deque()  # use a stack to store and update the intervals
    stack.append(list_pairs[0])
    for i in range(1, len(list_pairs)):
        front_i, rear_i = list_pairs[i]
        front, rear = stack[-1]
        if front_i <= rear:  # intervals should be updated because of overlap
            stack.pop()
            stack.append((min(front, front_i), max(rear_i, rear)))
        else:  # new intervals should be added
            stack.append(list_pairs[i])
    while len(stack) > 0:
        result.append(stack.pop())
    return result


if __name__ == "__main__":
    input_num1 = [(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]
    output1 = MergeIntervals(input_num1)
    input_num2 = [(5, 8), (6, 10), (2, 4), (3, 6)]
    output2 = MergeIntervals(input_num2)
    input_num3 = [(10, 12), (5, 6), (7, 9), (1, 3)]
    output3 = MergeIntervals(input_num3)
    print(output1)
    print(output2)
    print(output3)
