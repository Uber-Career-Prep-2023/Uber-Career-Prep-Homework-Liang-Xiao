class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.pre = None


# creates new Node with data val at front; returns new head
def insertAtFront(head, val):
    head1 = Node(val)
    head1.next = head
    head.pre = head1
    return head1


# creates new Node with data val at end
def insertAtBack(head, val):
    cur = head
    while cur.next is not None:
        cur = cur.next
    end = Node(val)
    cur.next = end
    end.pre = cur


# creates new Node with data val after Node loc
def insertAfter(head, val, loc):
    next_loc = loc.next
    new_node = Node(val)
    loc.next = new_node
    new_node.next = next_loc
    new_node.pre = loc
    next_loc.pre = new_node


# removes first Node; returns new head
def deleteFront(head):
    head1 = head.next
    head.next = None
    head1.pre = None
    return head1


# removes last Node
def deleteBack(head):
    if head.next is None:
        return None
    cur = head
    while cur.next.next is not None:
        cur = cur.next
    end = cur.next
    end.pre = None
    cur.next = None


# deletes Node loc; returns head
def deleteNode(head, loc):
    if loc is head:
        return deleteFront(head)
    prev = loc.pre
    nxt = loc.next
    prev.next = nxt
    nxt.pre = prev
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
        cur.pre = nxt
        pre = cur
        cur = nxt
    return pre


# reverses the linked list recursively
def reverseRecursive(head):
    if head.next is None:
        return head
    head1 = reverseRecursive(head.next)
    nxt = head.next
    head.next = None
    nxt.pre = None
    nxt.next = head
    head.pre = nxt
    return head1


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
    print("-----delete at back-----")
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


