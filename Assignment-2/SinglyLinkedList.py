class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self, node):
        self.head = node

    # creates new Node with data val at front; returns new head
    def insertAtFront(self, val):
        head1 = Node(val)
        head1.next = self.head
        self.head = head1
        return head1

    # creates new Node with data val at end
    def insertAtBack(self, val):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(val)

    # creates new Node with data val after location
    def insertAfter(self, val, loc):
        cur_loc = 0
        cur = self.head
        while cur_loc < loc:
            cur = cur.next
            cur_loc += 1
        nxt = cur.next
        new_node = Node(val)
        cur.next = new_node
        new_node.next = nxt

    # removes first Node; returns new head
    def deleteFront(self):
        head1 = self.head.next
        self.head.next = None
        self.head = head1
        return head1

    # removes last Node
    def deleteBack(self):
        if self.head.next is None:
            return None
        cur = self.head
        while cur.next.next is not None:
            cur = cur.next
        cur.next = None

    # deletes node at location; returns head
    def deleteNode(self, loc):
        if loc == 0:
            return self.deleteFront()

        cur_loc = 0
        pre = None
        cur = self.head
        while cur_loc < loc:
            pre = cur
            cur = cur.next
            cur_loc += 1
        nxt = cur.next
        pre.next = nxt

    #  returns length of the list
    def length(self):
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    #  reverses the linked list iteratively
    def reverseIterative(self):
        pre = None
        cur = self.head
        while cur is not None:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        self.head = pre
        return pre

    # reverses the linked list recursively
    def reverseRecursive(self):
        def reverse(head):
            if head.next is None:
                return head
            head1 = reverse(head.next)
            head.next.next = head
            head.next = None
            return head1
        self.head = reverse(self.head)

    def printList(self):
        print(self.head.val, end="")
        cur = self.head.next
        while cur is not None:
            print("-->" + str(cur.val), end="")
            cur = cur.next
        print()


if __name__ == "__main__":
    node1 = Node(1)
    slist1 = SinglyLinkedList(node1)
    num = [3, 5, 6, 8, 9]
    for ele in num:
        slist1.insertAtBack(ele)

    print("-----original list-----")
    slist1.printList()
    print("-----inset 7 at front-----")
    slist1.insertAtFront(7)
    slist1.printList()
    print("-----inset 8 after loc 2-----")
    slist1.insertAfter(8, 2)
    slist1.printList()
    print("-----delete at front-----")
    slist1.deleteFront()
    slist1.printList()
    print("-----delete at back-----")
    slist1.deleteBack()
    slist1.printList()
    print("-----delete loc 3 -----")
    slist1.deleteNode(3)
    slist1.printList()
    print("length of list is " + str(slist1.length()))
    print("-----reverse list iteratively-----")
    slist1.reverseIterative()
    slist1.printList()
    print("-----reverse list recursively-----")
    slist1.reverseRecursive()
    slist1.printList()
