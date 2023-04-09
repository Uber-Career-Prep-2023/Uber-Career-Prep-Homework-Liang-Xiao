class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# Given a sorted singly linked list, remove any duplicates so that no value appears more than once.

def DedupSortedList(head):
    if head.next is None:
        return
    pre = head
    cur = head.next
    while cur is not None:
        if cur.val != pre.val:
            pre.next = cur
            pre = cur
        cur = cur.next


# add a print method for testing
def printList(head):
    cur = head
    while cur.next is not None:
        print(str(cur.val) + "--->", end="")
        cur = cur.next
    print(str(cur.val))


if __name__ == "__main__":
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
    printList(head_node)
    DedupSortedList(head_node)
    printList(head_node)
