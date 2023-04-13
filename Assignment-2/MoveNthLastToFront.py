class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# Given a singly linked list, move the nth from the last element to the front of the list.
# assumption: n should less than the size of the list
# time complexity O(n), n refer to the number of node on the list
# space complexity O(1), extra space needed is constant
# time spent on the question: about 15 min

def MoveNthLastToFront(head, n):
    size = 0
    cur = head
    while cur is not None:  # calculate the size of the list
        size += 1
        cur = cur.next
    target_pos = size - n
    cur = head
    cur_pos = 0
    while cur_pos < target_pos:  # find the position before the target node
        cur_pos += 1
        cur = cur.next
    target = cur.next  # move the target node to the front
    cur.next = target.next
    target.next = head
    return target


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
    head_node = MoveNthLastToFront(head_node, 3)
    printList(head_node)
