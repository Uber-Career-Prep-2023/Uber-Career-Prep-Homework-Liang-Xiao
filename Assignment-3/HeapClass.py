import heapq


class minHeap:
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
    list_1 = [5, 9, 8, 4, 6, 1]
    heap_1 = minHeap(list_1)
    print(heap_1.top())
    heap_1.insert(7)
    heap_1.print_heap()
    heap_1.remove()
    heap_1.print_heap()
