"""
Given a string, return the string with the order of the space-separated words reversed
time complexity O(n), n refer to length of the input string
space complexity O(m), m refer to number of words in the input string
time spent on the question: about 10 min
"""


def ReverseWords(string):
    list_words = string.split()  # split the input str using " " to get a list of words
    output = []
    for i in range(len(list_words) - 1, -1, -1):  # traverse list of words backwards
        output.append(list_words[i])  # store the words in output list
    return " ".join(output)  # join the words in the output list using " "


if __name__ == "__main__":
    input_words = "Uber Career Prep"
    print(ReverseWords(input_words))
    input_words = "Emma lives in Brooklyn, New York."
    print(ReverseWords(input_words))
