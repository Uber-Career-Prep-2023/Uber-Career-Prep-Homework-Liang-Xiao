"""
# strategy: sort the interval by the low end and use a stack to store and update the intervals
1. sort the interval by the low end
2. create a stack and put the first interval into the stack
3. loop through the intervals, compare the current interval with the top of the stack, if there is
any overlap, pop the top, merge them and put the result in the stack
if no overlap, put the current interval in the stack
4. return the stack as all the merged intervals

# conditions to make sure : list_pairs is None or len(list_pairs) == 0

# time complexity: O(n), n refer to the length of list_pairs

# space complexity O(n), an extra list is added, n refer to the length of list_pairs

# time to complete, roughly 35 minutes, longer to think of the stack technique"""


def MergeIntervals(list_pairs):
    if list_pairs is None or len(list_pairs) == 0:
        return list_pairs

    def keyFun(input_list):
        return input_list[0]

    list_pairs.sort(key=keyFun)  # sort the interval by the low end
    stack = [list_pairs[0]]  # use a stack to store and update the intervals

    for i in range(1, len(list_pairs)):
        front_i, rear_i = list_pairs[i]
        front, rear = stack[-1]
        if front_i <= rear:  # intervals should be updated because of overlap
            del stack[-1]
            stack.append((min(front, front_i), max(rear_i, rear)))
        else:  # new intervals should be added
            stack.append(list_pairs[i])

    return stack


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
