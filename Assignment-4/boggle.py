"""
Boggle is a word game in which players compete to find the most words on a square grid of random letters.
Valid words must be at least three characters and formed from non-overlapping
(i.e., a position on the board can only be used once in a word) adjacent (including diagonal) letters.
Given a Boggle board and a dictionary of valid words, return all valid words on the board.
we first build a trie, then use dfs to traverse all words in the board
time complexity: build trie + dfs
build a trie: length of trie * length of a word
dfs: m * n * 8^(length of a word)
space complexity:build trie
O(num of chars in the trie )
time spent on the question: about 40 min
"""


class trie_node:
    def __init__(self, val=""):
        self.children = {}
        self.valid_word = False
        self.val = val


def boggle(board, dictionary):
    # A recursive function to print all words present on boggle
    def findWords(i, j, cur, m, n, node):
        # Mark current cell as visited and
        # append current character to str
        if visited[i][j]:
            return
        char = board[i][j]
        if char not in node.children:
            return
        node = node.children[char]
        cur.append(board[i][j])
        # If str is present in dictionary,append it in result
        if node.valid_word:
            res.append("".join(cur))

        visited[i][j] = True
        # Traverse 8 adjacent cells of boggle[i,j]
        row = i - 1
        while row <= i + 1 and row < m:
            col = j - 1
            while col <= j + 1 and col < n:
                if row >= 0 and col >= 0 and not visited[row][col]:
                    findWords(row, col, cur, m, n, node)
                col += 1
            row += 1

        # Erase current character from string and
        # mark visited of current cell as false
        del cur[-1]
        visited[i][j] = False

    # build a trie
    def build_trie(root_node, words):
        for word in words:
            cur = root_node
            """Insert a word into the trie"""
            # Loop through each character in the word
            # Check if there is no child containing the character, create a new child for the current node
            for char in word:
                if char in cur.children:
                    cur = cur.children[char]
                else:
                    # If a character is not found,
                    # create a new node in the trie
                    new_node = trie_node(char)
                    cur.children[char] = new_node
                    cur = new_node
            cur.valid_word = True
        return root_node

    root = trie_node()
    root = build_trie(root, dictionary)
    m = len(board)
    n = len(board[0])
    visited = [[False for _ in range(n)] for _ in range(m)]

    # Initialize current string
    start = []
    res = []
    # Consider every character and look for all words
    # starting with this character
    for i in range(m):
        for j in range(n):
            findWords(i, j, start, m, n, root)
    return res


if __name__ == "__main__":
    b = [["G", "I", "Z"], ["U", "E", "K"], ["Q", "S", "E"]]
    d = ["GEEKS", "FOR", "QUIZ", "GO"]
    print(boggle(b, d))
