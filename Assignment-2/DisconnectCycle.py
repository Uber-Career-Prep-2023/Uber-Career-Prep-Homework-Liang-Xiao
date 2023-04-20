class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# Given a singly linked list, disconnect the cycle, if one exists.
# time complexity O(n), n refer to the number of node on the list
# space complexity O(1), extra space needed is constant
# time spent on the question: about 35 min
def DisconnectCycle(head):
    fast = head
    slow = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            break
    # test whether a cycle exists
    if fast is None or fast.next is None:
        return
    # calculate where the last element is
    fast = head
    while fast.next is not slow.next:
        fast = fast.next
        slow = slow.next
    # disconnect the cycle
    slow.next = None


# add a print method for testing
def printList(head):
    cur = head
    while cur.next is not None:
        print(str(cur.val) + "--->", end="")
        cur = cur.next
    print(str(cur.val))


if __name__ == "__main__":
    # create a non-cycle list
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(2)
    node4 = Node(4)
    node5 = Node(4)
    node6 = Node(6)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    head_node = node1
    print("disconnect the cycle and print")
    DisconnectCycle(head_node)
    printList(head_node)
    # create a cycled list
    node1 = Node(1)
    node2 = Node(3)
    node3 = Node(8)
    node4 = Node(5)
    node5 = Node(4)
    node6 = Node(6)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node3 # there is a cycle in node3
    head_node = node1
    print("disconnect the cycle and print")
    DisconnectCycle(head_node)
    printList(head_node)

