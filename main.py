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
        self.map = {}

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
            self.map[self.array[iter].key], self.map[self.array[i_min].key] = self.map[self.array[i_min].key], self.map[
                self.array[iter].key]
            self.sift_down(i_min)

    def sift_up(self, iter):
        parent = int((iter - 1) / 2)

        if self.array[iter].key < self.array[parent].key:
            self.array[iter], self.array[parent] = self.array[parent], self.array[iter]
            self.map[self.array[iter].key], self.map[self.array[parent].key] = self.map[self.array[parent].key], \
                                                                               self.map[self.array[iter].key]
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
        self.map[node.key] = iter
        self.sift_up(iter)

    def extract(self):
        if self.size == 0:
            return None
        else:
            min = self.array[0]
            self.size -= 1
            self.array[0] = self.array[self.size]
            self.array.pop()
            self.map[self.array[0].key] = 0

            self.sift_down(0)
            return min

    def find(self, key):
        return self.map.get(key)

    def delete(self, key):
        iter = self.find(key)
        parent = int((iter - 1) / 2)
        left = 2 * iter + 1
        right = 2 * iter + 2

        self.array[iter], self.array[-1] = self.array[-1], self.array[iter]
        self.map[self.array[iter].key], self.map[self.array[-1].key] = self.map[self.array[-1].key], self.map[
            self.array[iter].key]

        self.array.pop()
        self.map.pop(key)
        self.size -= 1

        if iter < self.size:
            if self.array[iter].key < self.array[parent].key:
                self.sift_up(iter)
            else:
                if left < self.size:
                    if self.array[iter].key > self.array[left].key:
                        self.sift_down(iter)
                if right < self.size:
                    if self.array[iter].key > self.array[right].key:
                        self.sift_down(iter)

    def get_min(self):
        if self.size:
            return str(self.array[0].key) + ' 0 ' + str(self.array[0].value)
        return None

    def get_max(self):
        last_parent = int(self.size / 2) - 1
        last_level = self.array[last_parent + 1: self.size]
        max = last_level[0]
        for elem in last_level:
            if elem.key > max.key:
                max = elem
        return str(max.key) + ' ' + str(self.map[max.key]) + ' ' + str(max.value)

    def set(self, key, new_val):
        iter = self.map[key]
        self.array[iter].value = new_val

    def print_level(self, start, end, level_number, out):
        if end < self.size:
            level = self.array[start:end + 1]
        else:
            level = self.array[start:self.size]
            for j in range(end - self.size + 1):
                level.append('_')

        for i in range(len(level)):
            if isinstance(level[i], Node):
                level[i].parent = self.array[int((i - 1) / 2)]
            print(str(level[i]), end=' ', file=out)
        print()
        if end < self.size - 1:
            level_number += 1

            self.print_level(end + 1, end + 2 ^ level_number, level_number, out)

    def print_heap(self, out):
        if self.array:
            print(str(self.array[0]), file=out)
            start = 1
            end = start * 2
            level_number = 1
            self.print_level(start, end, level_number, out)
        else:
            print('error', file=out)


def main():
    heap = MyHeap()
    # MyHeap.build_heap(heap, list)
    heap.insert(6, 1)
    heap.insert(14, 1)
    heap.insert(10, 1)
    heap.insert(8, 1)
    heap.insert(7, 1)
    heap.insert(11, 1)
    heap.delete(11)
    heap.extract()

    heap.print_heap(sys.stdout)

    print(str(heap.get_max()))

    for line in sys.stdin:
        line = line.rstrip('\r\n')
        if "add" in line:
            if len(line.split()) == 3:
                heap.insert(line.split()[1], line.split()[2])
            else:
                print("error", file=sys.stdout)

        elif "set" in line:
            if len(line.split()) == 3 and heap.size:
                heap.set(line.split()[1], line.split()[2])
            else:
                print("error", file=sys.stdout)

        elif "delete" in line:
            if len(line.split()) == 2:
                if heap.size:
                    heap.delete(line.split()[1])
                else:
                    print("error", file=sys.stdout)
            else:
                print("error", file=sys.stdout)

        elif "search " in line:
            if heap.size == 0:
                print('0', file=sys.stdout)
            elif len(line.split()) == 2:
                node_iter = heap.find(line.split()[1])
                if not node_iter:
                    print('0', file=sys.stdout)
                else:
                    print('1 ' + str(node_iter) + ' ' + str(heap.array[node_iter].value), file=sys.stdout)
            else:
                print("error", file=sys.stdout)

        elif "min" == line:
            if heap.size:
                print(heap.get_min(), file=sys.stdout)
            else:
                print("error", file=sys.stdout)

        elif "max" == line:
            if heap.size:
                print(heap.get_max(), file=sys.stdout)
            else:
                print("error", file=sys.stdout)

        elif "extract" == line:
            if heap.size:
                node = heap.extract()
                print(str(node.key) + ' ' + str(node.value), file=sys.stdout)

        elif line == "print":
            heap.print_heap(sys.stdout)

        elif not (line and line.strip()):
            continue
        else:
            print("error", file=sys.stdout)


main()
