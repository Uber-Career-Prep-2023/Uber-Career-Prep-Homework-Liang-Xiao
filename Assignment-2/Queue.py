from collections import deque


class Queue:
    def __init__(self):
        self.dq = deque()

    # returns the first item in the queue
    def peek(self):
        return self.dq[0]

    # adds x to the back of the queue
    def enqueue(self, x):
        self.dq.append(x)

    # removes and returns the first item in the queue
    def dequeue(self):
        return self.dq.popleft()

    # returns a boolean indicating whether the queue is empty
    def isEmpty(self):
        return len(self.dq) == 0

    def print(self):
        print(self.dq)


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
