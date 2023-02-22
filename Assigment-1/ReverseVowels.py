"""
# strategy: using a list to store the sequence of vowels and output them reversely.
 1. loop through the input string and collect vowels in a list
 2. create an output list to store the elements of output string as string is immutable
 3. loop through the input string from left to right and replace vowels with the elements in the list
     from the right to left
 4. convert the output list into a string

# base cases : input is none or empty or no vowels, just return the input itself

# time complexity: O(n), n refer to the length of the input string

# space complexity O(n), an array added to store the sequence of vowels

# time to complete, roughly 20 minutes"""


def reverse_vowels(string_input):
    if string_input is None or len(string_input) == 0:
        return string_input
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    input_vowels = []  # create a list to store vowels
    for ele in string_input:  # loop the string and store vowels in a list
        if ele in vowels:
            input_vowels.append(ele)

    if len(input_vowels) == 0:
        return string_input

    pos = len(input_vowels) - 1  # begin with the last element in the list
    list_output = []  # create an output list to store the result
    for i in range(len(string_input)):
        if string_input[i] in vowels:
            list_output.append(input_vowels[pos])  # loop the vowel list reversely
            pos -= 1
        else:
            list_output.append(string_input[i])
    return "".join(list_output)


if __name__ == "__main__":
    str1 = "Uber Career Prep"
    str2 = "xyz"
    str3 = "flamingo"
    print(reverse_vowels(str1))
    print(reverse_vowels(str2))
    print(reverse_vowels(str3))
