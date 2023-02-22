"""
# strategy: using a dictionary to store the occurrence of element in str1, then traverse str2 and count the difference
1. using a dictionary to store the occurrence of element in str1
2. traverse str2 and match the elements in the dictionary and the update the value
3. traverse key value pair of the dictionary and add up all the positive value as the total difference as the
positive value means count of elements that need to be matched


# base cases : input strings are None or their length not equal

# time complexity: O(n), n refer to the length of the str1 and str2, len(str1) = len(str2)

# space complexity O(n), a dictionary is added as the length of the str1

# time to complete, roughly 20 minutes"""


def KAnagrams(str1, str2, k):
    # three base cases as below
    if str1 is None and str2 is None:
        return True
    if str1 is None or str2 is None:
        return False
    if len(str1) != len(str2):
        return False
    # use a dictionary to store the occurrence of element in str1
    dict_1 = {}
    difference = 0
    for ele in str1:
        if ele not in dict_1:
            dict_1[ele] = 1
        else:
            dict_1[ele] += 1
    # traverse str2 and update the value of each element
    for ele in str2:
        if ele in dict_1:
            dict_1[ele] -= 1
    # traverse dict_1 to count the total difference
    for key, val in dict_1.items():
        if val > 0:  # add up the positive value
            difference += val
    return difference <= k


if __name__ == "__main__":
    res1 = KAnagrams("apple", "peach", 1)
    res2 = KAnagrams("apple", "peach", 2)
    res3 = KAnagrams("cat", "dog", 3)
    res4 = KAnagrams("debit curd", "bad credit", 1)
    res5 = KAnagrams("baseball", "basketball", 2)
    print(res1)
    print(res2)
    print(res3)
    print(res4)
    print(res5)
