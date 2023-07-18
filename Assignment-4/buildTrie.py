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
        if node.valid_word:
            return True
        return False

    def remove(self, word):
        if not self.is_valid_word(word):
            return

        node = self.root

        # Loop through each character in the word
        # Check if the node containing the character has only one or no child, delete that node
        for char in word:
            if char in node.children:
                nxt = node.children[char]
                if len(nxt.children) < 1:
                    node.children.pop(char)
                    return
                node = nxt


if __name__ == "__main__":
    words = trie()
    words.insert('was')
    words.insert('what')
    words.insert('where')
    words.insert('wet')
    words.insert('wash')
    print(words.is_valid_word('was'))
    print(words.is_valid_word('wat'))
    print(words.is_valid_word('what'))
    words.remove('what')
    print(words.is_valid_word('wa'))
    print(words.is_valid_word('what'))
