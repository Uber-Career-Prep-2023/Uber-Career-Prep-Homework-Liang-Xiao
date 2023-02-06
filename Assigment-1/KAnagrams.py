# strategy: using a dictionary to store the occurrence of element in str1, then traverse str2
#           and count the difference
# base cases : seen in below
# time complexity: O(m + n + m), m refer to the length of the str1 and n refer to the length of the str2
# space complexity O(n), a dictionary is added
# time to complete, roughly 20 minutes
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
    # traverse str2 and store the difference of each element
    for ele in str2:
        if ele in dict_1:
            dict_1[ele] -= 1
    # traverse dict_1 to count the total difference
    for key in dict_1:
        difference += abs(dict_1[key])
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
