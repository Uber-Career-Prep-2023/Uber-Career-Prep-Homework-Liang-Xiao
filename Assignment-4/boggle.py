class trie_node:
    def __init__(self, val=""):
        self.children = {}
        self.valid_word = False
        self.val = val


class trie:
    def __init__(self):
        self.root = trie_node()

    def insert(self, word):
        """Insert a word into the trie"""
        node = self.root

        # Loop through each character in the word
        # Check if there is no child containing the character, create a new child for the current node
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # If a character is not found,
                # create a new node in the trie
                new_node = trie_node(char)
                node.children[char] = new_node
                node = new_node

        # Mark the end of a word
        node.valid_word = True

    def is_valid_word(self, word):
        node = self.root

        # Loop through each character in the word
        # Check if there is no child containing the character, return false.
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return True


def boggle(board, dictionary):
    # A recursive function to print all words present on boggle
    def findWords(i, j, cur, m, n):
        # Mark current cell as visited and
        # append current character to str
        visited[i][j] = True
        cur.append(board[i][j])

        # If str is present in dictionary,append it in result
        if len(cur) >= 3 and words.is_valid_word("".join(cur)):
            res.append("".join(cur))

        # Traverse 8 adjacent cells of boggle[i,j]
        row = i - 1
        while row <= i + 1 and row < m:
            col = j - 1
            while col <= j + 1 and col < n:
                if row >= 0 and col >= 0 and not visited[row][col]:
                    findWords(row, col, cur, m, n)
                col += 1
            row += 1

        # Erase current character from string and
        # mark visited of current cell as false
        del cur[-1]
        visited[i][j] = False

    words = trie()
    for word in dictionary:
        words.insert(word)
    m = len(board)
    n = len(board[0])
    visited = [[False for i in range(n)] for j in range(m)]

    # Initialize current string
    start = []
    res = []
    # Consider every character and look for all words
    # starting with this character
    for i in range(m):
        for j in range(n):
            findWords(i, j, start, m, n)


if __name__ == "__main__":
    board = [["G", "I", "Z"], ["U", "E", "K"], ["Q", "S", "E"]]
    dictionary = ["GEEKS", "FOR", "QUIZ", "GO"]
    print(boggle(board, dictionary))
