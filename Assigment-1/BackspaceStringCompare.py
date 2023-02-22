"""
#strategy: using two extra lists to store the elements of the strings
 1. create two lists to store the elements of the strings
 2. loop the inputs string and fill in the lists, when coming across #, delete the last element in the list
 3. check whether the elements in two lists are same

# conditions to make sure : whether input are none or empty strings
                           the index and number of # is valid to makes sure there are enough chars to be deleted

# time complexity: O(m + n), m and n refer to the length of the input strings

# space complexity O(m + n), two lists added to store elements of the strings

# time to complete, roughly 15 minutes."""


def BackspaceStringCompare(input_str1, input_str2):
    if input_str1 is None and input_str2 is None:
        return True
    if input_str1 is None or input_str2 is None:
        return False
    # two extra array to store the elements of the strings
    list1 = []
    list2 = []
    # loop the inputs string and fill in the lists
    for ele in input_str1:
        if ele == "#":
            del list1[-1]  # when coming across #, delete the last element in the list
        else:
            list1.append(ele)
    for ele in input_str2:
        if ele == "#":
            del list2[-1]  # when coming across #, delete the last element in the list
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
