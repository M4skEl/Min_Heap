import sys


class Node:
    def __init__(self, key, val, parent=None):
        self.key = key
        self.value = val
        self.parent = parent

    def __str__(self):
        if not self:
            return '_'
        if self.parent:
            return f"[{self.key} {self.value} {self.parent.key}]"
        else:
            return f"[{self.key} {self.value}]"


class MyHeap:
    def __init__(self):
        self.array = []
        self.size = 0

    def sift_down(self, iter):
        left = 2 * iter + 1
        right = 2 * iter + 2
        i_min = iter

        if left < self.size and self.array[left].key < self.array[iter].key:
            i_min = left

        if right < self.size and self.array[right].key < self.array[iter].key:
            i_min = right

        if i_min != iter:
            self.array[iter], self.array[i_min] = self.array[i_min], self.array[iter]
            self.sift_down(i_min)

    def sift_up(self, iter):
        parent = int((iter - 1) / 2)

        if self.array[iter].key < self.array[parent].key:
            self.array[iter], self.array[parent] = self.array[parent], self.array[iter]
            self.sift_up(parent)

    def build_heap(self, arr):
        self.size = len(arr)
        self.array = arr
        last_parent = int(self.size / 2)
        for i in range(last_parent):
            self.sift_down(i)

    def insert(self, key, value):
        iter = self.size
        self.size += 1
        node = Node(key, value)
        self.array.append(node)
        self.sift_up(iter)

    def extract(self):
        if self.size == 0:
            return None
        else:
            min = self.array[0]
            self.size -= 1
            self.array[0] = self.array[self.size - 1]
            self.sift_down(0)
            return min


def main():
    # list = [6, 14, 10, 8, 7, 11]
    heap = MyHeap()
    # MyHeap.build_heap(heap, list)
    heap.insert(6, 1)
    heap.insert(14, 1)
    heap.insert(10, 1)
    heap.insert(8, 1)
    heap.insert(7, 1)
    heap.insert(11, 1)
    print(heap.array[0])
    print(heap.array[1])
    print(heap.array[2])
    print(heap.array[3])
    print(heap.array[4])
    print(heap.array[5])


main()
