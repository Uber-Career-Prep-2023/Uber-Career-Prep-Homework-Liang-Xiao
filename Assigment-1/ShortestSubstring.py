"""
# strategy: using a dictionary to store the occurrence of elements in target string
           and use sliding window strategy to find the shortest substring
1. create a dictionary to store the occurrence of elements in target string
2. create a head and tail pointer to represent a sliding window
3. use a counter to keep track of elements left to contain in the window
3. move the tail pointer to enlarge the window until it contains the target string in the window
4. move the head pointer to shrink the window and update the shortest length of the window
until it doesn't contain the target string in the window
5. repeat 3 and 4 until the tail pointer reach the end

# conditions to make sure :
           the target string must be a substring of the input string
           if the target string is empty string return 0

# time complexity: O(m + n), m and n refer to the length of the input string and target string

# space complexity O(n), an extra dictionary is added as length of target string

# time to complete, roughly 35 minutes, longer to think out how to move the pointers"""


def ShortestSubstring(input_str, target_str):
    if len(target_str) == 0:
        return 0
    dict_count = {}
    for ele in target_str:
        if ele in dict_count:
            dict_count[ele] += 1
        else:
            dict_count[ele] = 1
    pointer_head = 0
    pointer_tail = 0
    count = len(dict_count)  # num of elements to be matches
    shortest = len(input_str)
    while pointer_tail < len(input_str):
        # move the tail pointer to find a substring that contains target
        tail = input_str[pointer_tail]
        if tail in dict_count:
            dict_count[tail] -= 1
            if dict_count[tail] == 0:
                count -= 1
        pointer_tail += 1
        # move the head pointer to make the substring shorter until it doesn't contain the target,
        # and the following while loop will break
        # back to the outer while loop and continue moving the tail pointer
        while count == 0:
            shortest = min(shortest, pointer_tail - pointer_head)
            head = input_str[pointer_head]
            if head in dict_count and dict_count[head] == 0:
                dict_count[head] = 1
                count = 1
            pointer_head += 1
    return shortest


if __name__ == "__main__":
    str1, str2 = "abracadabra", "abc"
    print(ShortestSubstring(str1, str2))
    str1, str2 = "zxycbaabcdwxyzzxwdcbxyzabccbazyx", "zzyzx"
    print(ShortestSubstring(str1, str2))
    str1, str2 = "dog", "god"
    print(ShortestSubstring(str1, str2))
