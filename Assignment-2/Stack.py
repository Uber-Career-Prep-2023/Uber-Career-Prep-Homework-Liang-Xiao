class Stack:
    def __init__(self):
        self.stack = []

    #  returns the top item in the stack
    def top(self):
        return self.stack[-1]

    # adds x to the top of the stack
    def push(self, x):
        self.stack.append(x)

    # removes and returns the top item in the stack
    def pop(self):
        return self.stack.pop()

    # returns a boolean indicating whether the stack is empty
    def isEmpty(self):
        return len(self.stack) == 0

    # returns a boolean indicating whether the stack is empty
    def print(self):
        print(self.stack)


if __name__ == "__main__":
    # create a stack
    stack = Stack()
    # add some element into stack
    stack.push(1)
    stack.push(4)
    stack.push(5)
    stack.push(3)
    stack.push(8)
    # print the stack
    stack.print()
    # print the first element stack
    print(stack.top())
    # remove element from the stack
    top = stack.pop()
    print(top)
    # print the stack
    stack.print()
    # check if the queue is empty
    print(stack.isEmpty())
