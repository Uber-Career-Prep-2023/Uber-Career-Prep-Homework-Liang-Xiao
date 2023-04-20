class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.pre = None


# Given a doubly linked list, determine if it is a palindrome.
# time complexity O(n), n refer to the number of node on the list
# space complexity O(1), extra space needed is constant
# time spent on the question: about 15 min

def IsPalindrome(head):
    end = head
    while end.next is not None:
        end = end.next
    while head is not end and end.next is not head:
        if head.val != end.val:
            return False
        head = head.next
        end = end.pre
    return True


# add a printing method to show the values of nodes on the list for testing
def printList(head):
    cur = head
    while cur.next is not None:
        print(str(cur.val) + "--->", end="")
        cur = cur.next
    print(str(cur.val))
    res = str(cur.val)
    cur = cur.pre
    while cur is not None:
        res = str(cur.val) + "<---" + res
        cur = cur.pre
    print(res)


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node1.next = node2
    node2.pre = node1
    node2.next = node3
    node3.pre = node2
    node3.next = node4
    node4.pre = node3
    node4.next = node5
    node5.pre = node4
    node5.next = node6
    node6.pre = node5
    print("-----original list-----")
    printList(node1)
    print(IsPalindrome(node1))
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(3)
    node5 = Node(2)
    node6 = Node(1)
    node1.next = node2
    node2.pre = node1
    node2.next = node3
    node3.pre = node2
    node3.next = node4
    node4.pre = node3
    node4.next = node5
    node5.pre = node4
    node5.next = node6
    node6.pre = node5
    print("-----original list-----")
    printList(node1)
    print(IsPalindrome(node1))
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(2)
    node5 = Node(1)
    node1.next = node2
    node2.pre = node1
    node2.next = node3
    node3.pre = node2
    node3.next = node4
    node4.pre = node3
    node4.next = node5
    node5.pre = node4
    print("-----original list-----")
    printList(node1)
    print(IsPalindrome(node1))

