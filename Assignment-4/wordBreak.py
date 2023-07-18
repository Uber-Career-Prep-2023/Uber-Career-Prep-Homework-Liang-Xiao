"""
Given a string of characters without spaces and a dictionary of valid words,
determine if it can be broken into a list of valid words by adding spaces.ase?

we use dynamic programming, dp[i] means whether it can be broken into a list of valid
word from string indexing [0, i), and dp[j] = dp[i] and string[i:j] (i < j)
time complexity O(n2), n refer to size of the string
space complexity O(n), an extra array of n is needed
time spent on the question: about 15 min"""


def wordBreak(string, words):
    words = set(words)
    n = len(string)
    dp = [False for _ in range(n + 1)]
    dp[0] = True
    for i in range(n):
        for j in range(i + 1, n + 1):
            if dp[i] and string[i:j] in words:
                dp[j] = True
    return dp[-1]


if __name__ == "__main__":
    dictionary = ['elf', 'go', 'golf', 'man', 'manatee', 'not', 'note', 'pig', 'quip', 'tee', 'teen']
    string1 = 'mangolf'
    print(wordBreak(string1, dictionary))
    string1 = 'manateenotelf'
    print(wordBreak(string1, dictionary))
    string1 = 'quipig'
    print(wordBreak(string1, dictionary))
