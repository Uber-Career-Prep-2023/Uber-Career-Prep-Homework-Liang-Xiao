class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Given a target numeric value and a binary search tree,
# return the floor (the greatest element less than or equal to the target) in the BST.
# time complexity O(h), h refer to the height on the tree
# space complexity O(1), constant space is needed
# time spent on the question: about 15 min

def FloorInBST(root, target):
    cur = root
    res = cur.val
    while cur is not None:
        if cur.val == target:
            res = cur.val
            return res
        elif cur.val > target:
            res = cur.val
            cur = cur.left
        else:
            cur = cur.right
    return res


if __name__ == "__main__":
    node1 = TreeNode(10)
    node2 = TreeNode(8)
    node3 = TreeNode(16)
    node4 = TreeNode(9)
    node5 = TreeNode(13)
    node6 = TreeNode(17)
    node7 = TreeNode(20)
    # construct a bst for testing
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node3.left = node5
    node3.right = node6
    node6.right = node7
    root_node = node1
    # find the floor of 13 and 15 in bst
    print(FloorInBST(root_node, 13))
    print(FloorInBST(root_node, 15))
