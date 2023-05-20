import heapq


class PriorityQueue:
    def __init__(self, arr):
        heapq.heapify(arr)
        self.arr = arr

    def top(self):
        return self.arr[0]

    def insert(self, x):
        heapq.heappush(self.arr, x)

    def remove(self):
        return heapq.heappop(self.arr)

    def print_heap(self):
        print(self.arr)


if __name__ == "__main__":
    list_1 = [(7,'Rina'),(1,'Anish'),(8,'Moana'),(2,'cathy'),(4,'Lucy')]
    pq_1 = PriorityQueue(list_1)
    print(pq_1.top())
    pq_1.insert((5, 'asher'))
    pq_1.print_heap()
    pq_1.remove()
    pq_1.print_heap()
