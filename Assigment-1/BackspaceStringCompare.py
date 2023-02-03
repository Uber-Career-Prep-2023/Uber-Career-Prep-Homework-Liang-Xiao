# strategy: using two extra array to decode the elements of the strings
# conditions to make sure : input is none or empty string, just return 0
#                           the index of # is valid
# time complexity: O(n1 + n2), n1 and n2 refer to the length of the input strings
# space complexity O(n1 + n2), two lists added to store elements of the strings
# time to complete, roughly 15 minutes.
def BackspaceStringCompare(str1, str2):
    if str1 is None and str2 is None:
        return True
    if str1 is None or str2 is None:
        return False
    list1 = []
    list2 = []
    for ele in str1:
        if ele == "#":
            del list1[-1]
        else:
            list1.append(ele)
    for ele in str2:
        if ele == "#":
            del list2[-1]
        else:
            list2.append(ele)
    return list1 == list2


if __name__ == "__main__":
    str1, str2 = "abcde", "abcde"
    print(BackspaceStringCompare(str1, str2))
    str1, str2 = "Uber Career Prep", "u#Uber Careee#r Prep"
    print(BackspaceStringCompare(str1, str2))
    str1, str2 = "abcdef###xyz", "abcw#xyz"
    print(BackspaceStringCompare(str1, str2))
    str1, str2 = "abcdef###xyz", "abcdefxyz###"
    print(BackspaceStringCompare(str1, str2))
