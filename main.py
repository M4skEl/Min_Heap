import sys


class MyHeap:
    def __init__(self):
        self.array = None
        self.size = None

    def sift_down(self, iter):
        left = 2 * iter + 1
        right = 2 * iter + 2
        i_min = iter

        if left < self.size and self.array[left] < self.array[iter]:
            i_min = left

        if right < self.size and self.array[right] < self.array[iter]:
            i_min = right

        if i_min != iter:
            self.array[iter], self.array[i_min] = self.array[i_min], self.array[iter]
            self.sift_down(i_min)

    def sift_up(self, iter):
        pass

    def build_heap(self, arr):
        self.size = len(arr)
        self.array = arr
        last_parent = int(self.size / 2)
        for i in range(last_parent):
            self.sift_down(i)


def main():
    list = [6, 14, 10, 8, 7, 11]
    heap = MyHeap()
    MyHeap.build_heap(heap, list)

    print(heap.array)



main()
