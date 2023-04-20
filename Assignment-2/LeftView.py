from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Given a binary tree, create an array of the left view (leftmost elements in each level) of the tree.
# time complexity O(n), n refer to the number of node on the tree
# space complexity O(l), l refer to the largest number of nodes in each level of the tree
# time spent on the question: about 15 min
def LeftView(root):
    result = []
    level_node = deque()
    level_node.append(root)
    while len(level_node) > 0:
        size = len(level_node)
        for i in range(size):
            node = level_node.popleft()
            if i == 0:
                result.append(node.val)
            if node.left is not None:
                level_node.append(node.left)
            if node.right is not None:
                level_node.append(node.right)
    return result


if __name__ == "__main__":
    node1 = TreeNode(5)
    node2 = TreeNode(3)
    node3 = TreeNode(2)
    node4 = TreeNode(4)
    node5 = TreeNode(1)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node3.right = node5
    tree_root = node1
    print(LeftView(tree_root))

