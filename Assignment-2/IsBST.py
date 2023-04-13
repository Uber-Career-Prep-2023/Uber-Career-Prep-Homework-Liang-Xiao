class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Given a binary tree, determine if it is a binary search tree.
# time complexity O(n), n refer to the number of node on the tree
# space complexity O(log(n)), n refer to the number of node on the tree
# time spent on the question: about 20 min
def isBst(root):
    def helper(tree_root, min_val, max_val):
        if tree_root is None:
            return True
        if tree_root.val > max_val or tree_root.val < min_val:
            return False
        return helper(tree_root.left, min_val, root.val) and helper(tree_root.right, root.val, max_val)

    return helper(root, float("-inf"), float("inf"))


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
    node3 = TreeNode(8)
    node4 = TreeNode(2)
    node5 = TreeNode(10)
    # construct a bst for testing
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node3.right = node5
    root_node = node1
    print(traverse(root_node))
    print(isBst(root_node))
    # rearrange the bst to test if it's still bst
    node1.right = node4
    node2.left = node3
    print(traverse(root_node))
    print(isBst(root_node))
