class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, root):
        self.root = root

    # returns the minimum value in the BST
    def min(self):
        cur = self.root
        while cur.left is not None:
            cur = cur.left
        return cur.val

    # returns the maximum value in the BST
    def max(self):
        cur = self.root
        while cur.right is not None:
            cur = cur.right
        return cur.val

    # returns a boolean indicating whether val is present in the BST
    def contains(self, val):
        node = self.root
        while node is not None:
            if node.val > val:
                node = node.left
            elif node.val < val:
                node = node.right
            else:
                return True
        return False

    # creates a new Node with data val in the appropriate location,
    # For simplicity, do not allow duplicates. If val is already present, insert is a no-op
    def insert(self, val):
        def insert(root, value):
            if root is None:
                return TreeNode(val)
            if root.val > value:
                root.left = insert(root.left, value)
            elif root.val < value:
                root.right = insert(root.right, value)
            return root

        self.root = insert(self.root, val)

    # deletes the Node with data val, if it exists
    # For simplicity, do not allow duplicates. if it doesn't exist, return -1
    def delete(self, val):
        def deleteLargest(node):
            cur = node
            while cur.right.right is not None:
                cur = cur.right
            largest = cur.right
            cur.right = largest.left
            return largest.val

        def deleteNode(node, target):
            if node is None:
                return None
            if node.val < target:
                node.right = deleteNode(node.right, target)
            elif node.val > target:
                node.left = deleteNode(node.left, target)
            else:
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                if node.left.right is None:
                    node.left.right = node.right
                    return node.left
                node.val = deleteLargest(node.left)
            return node

        self.root = deleteNode(self.root, val)

    # add a traverse to show the values of nodes on the tree for testing
    def traverse(self):
        def helper(node, res):
            if node is None:
                return
            helper(node.left, res)
            res.append(node.val)
            helper(node.right, res)

        tree_list = []
        helper(self.root, tree_list)
        return tree_list


if __name__ == "__main__":
    tree_root = TreeNode(5)
    tree = BinarySearchTree(tree_root)
    tree.insert(3)
    tree.insert(2)
    tree.insert(8)
    tree.insert(6)
    tree.insert(12)
    tree.insert(7)
    tree.insert(5)
    print(tree.traverse())
    print(tree.min())
    print(tree.max())
    tree.delete(8)
    print(tree.traverse())
