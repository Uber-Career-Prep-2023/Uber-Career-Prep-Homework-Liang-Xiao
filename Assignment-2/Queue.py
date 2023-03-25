class Queue:
    def __init__(self):
        self.list1 = []
        self.list2 = []

    # returns the first item in the queue
    def peek(self):
        if len(self.list2) > 0:
            return self.list2[-1]
        while len(self.list1) > 0:
            self.list2.append(self.list1.pop())
        return self.list2[-1]

    # adds x to the back of the queue
    def enqueue(self, x):
        self.list1.append(x)

    # removes and returns the first item in the queue
    def dequeue(self):
        res = self.peek()
        self.list2.pop()
        return res

    # returns a boolean indicating whether the queue is empty
    def isEmpty(self):
        return len(self.list1) + len(self.list2) == 0

    def print(self):
        for i in range(len(self.list2) - 1, -1, -1):
            print(f"{self.list2[i]} ", end="")
        for i in range(len(self.list1)):
            print(f"{self.list1[i]} ", end="")
        print()


if __name__ == "__main__":
    # create a queue
    queue = Queue()
    # add some element into queue
    queue.enqueue(1)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(3)
    queue.enqueue(8)
    # print the queue in order
    queue.print()
    # print the first element queue
    print(queue.peek())
    # remove element from the queue
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    # print the first element queue
    print(queue.peek())
    # print the queue in order
    queue.print()
    # check if the queue is empty
    print(queue.isEmpty())
