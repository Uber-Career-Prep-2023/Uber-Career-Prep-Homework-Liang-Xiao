class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Given a binary tree, create a deep copy. Return the root of the new tree.
# time complexity O(n), n refer to the number of node on the tree
# space complexity O(n), n refer to the number of node on the tree
# time spent on the question: about 10 min
def CopyTree(root):
    if root is None:
        return None
    root_copy = TreeNode(root.val)
    root_copy.left = CopyTree(root.left)
    root_copy.right = CopyTree(root.right)
    return root_copy


# add a traverse method to show the values of nodes on the tree for testing

def traverse(root):
    def helper(node, res):
        if node is None:
            return
        helper(node.left, res)
        res.append(node.val)
        helper(node.right, res)

    tree_list = []
    helper(root, tree_list)
    return tree_list


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
    root1 = node1
    root2 = CopyTree(root1)
    print(traverse(root1))
    print(traverse(root2))
    # rearrange the nodes on root1 will not affect root2 because of deep copy
    node1.right = node4
    node2.left = node3
    print(traverse(root1))
    print(traverse(root2))
