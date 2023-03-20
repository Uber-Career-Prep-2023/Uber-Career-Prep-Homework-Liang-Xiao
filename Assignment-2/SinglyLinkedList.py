class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# creates new Node with data val at front; returns new head
def insertAtFront(head, val):
    head1 = Node(val)
    head1.next = head
    return head1


# creates new Node with data val at end
def insertAtBack(head, val):
    cur = head
    while cur.next is not None:
        cur = cur.next
    cur.next = Node(val)


# creates new Node with data val after Node loc
def insertAfter(head, val, loc):
    next_loc = loc.next
    new_node = Node(val)
    loc.next = new_node
    new_node.next = next_loc


# removes first Node; returns new head
def deleteFront(head):
    head1 = head.next
    head.next = None
    return head1


# removes last Node
def deleteBack(head):
    if head.next is None:
        return None
    cur = head
    while cur.next.next is not None:
        cur = cur.next
    cur.next = None


# deletes Node loc; returns head
def deleteNode(head, loc):
    if loc is head:
        return deleteFront(head)
    cur = head
    while cur.next is not loc:
        cur = cur.next
    cur.next = loc.next
    return head


#  returns length of the list
def length(head):
    cur = head
    count = 0
    while cur is not None:
        count += 1
        cur = cur.next
    return count


#  reverses the linked list iteratively
def reverseIterative(head):
    pre = None
    cur = head
    while cur is not None:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    return pre


# reverses the linked list recursively
def reverseRecursive(head):
    if head.next is None:
        return head
    head1 = reverseRecursive(head.next)
    head.next.next = head
    head.next = None
    return head1


def printList(head):
    print(head.val, end="")
    head = head.next
    while head is not None:
        print("-->" + str(head.val), end="")
        head = head.next
    print()


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    print("-----original list-----")
    printList(node1)
    print("-----inset 7 at front-----")
    new_head = insertAtFront(node1, 7)
    printList(new_head)
    print("-----inset 8 after node2-----")
    insertAfter(new_head, 8, node2)
    printList(new_head)
    print("-----inset 9 at back-----")
    insertAtBack(new_head, 9)
    printList(new_head)
    print("-----delete at front-----")
    new_head = deleteFront(new_head)
    printList(new_head)
    print("-----delete at front-----")
    deleteBack(new_head)
    printList(new_head)
    print("-----delete node3 -----")
    new_head = deleteNode(new_head, node3)
    printList(new_head)
    print("length of list is " + str(length(new_head)))
    print("-----reverse list iteratively-----")
    new_head = reverseIterative(new_head)
    printList(new_head)
    print("-----reverse list recursively-----")
    new_head = reverseIterative(new_head)
    printList(new_head)


