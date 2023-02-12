# strategy: using a dictionary to store the occurrence of elements in input strings
#           and use sliding window strategy to find the shortest substring
# conditions to make sure :
#            the target string must be a substring of the input string
#            if the target string is empty string return 0
# time complexity: O(n1 + n2), n1 and n2 refer to the length of the input strings
# space complexity O(n2), an extra dictionary is added
# time to complete, roughly 35 minutes, longer to think out how to move the pointers
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
        # and second while loop will break
        # back to the first while loop and continue moving the tail pointer
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
