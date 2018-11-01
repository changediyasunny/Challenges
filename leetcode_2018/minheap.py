"""

"""

import sys, os
from collections import defaultdict


class MinHeap(object):

    def __init__(self, array):
        self.array = array
        self.heap_size = len(self.array)
        self.build_min_heap()
        print("=========FINAL============")
        print(self.array)

    def parent(self, i):
        return (i-1)//2

    def left(self, i):
        return (2*i + 1)

    def right(self, i):
        return 2 * (i + 1)

    def build_min_heap(self):
        for i in range(N//2)[::-1]:
            self.min_heapify(i)

    def min_heapify(self, i):
        print(self.array)
        print("====================")
        l = self.left(i)
        r = self.right(i)
        print(i, l, r)
        if l <= self.heap_size and self.array[l] < self.array[i]:
            smallest = l
        else:
            smallest = i

        if r <= self.heap_size and self.array[r] < self.array[smallest]:
            smallest = r
        if smallest != i:
            temp = self.array[i]
            self.array[i] = self.array[smallest]
            self.array[smallest] = temp
            self.min_heapify(smallest)

    def heapsort(self):
        print("===on heap sort=======")
        for i in range(N-1, 0, -1):
            temp = self.array[0]
            self.array[0] = self.array[i]
            self.array[i] = temp
            self.heap_size = self.heap_size - 1
            self.min_heapify(0)
        print("sorted array: ")
        print(self.array)

arr = [5, 13, 82, 25, 7, 17, 20, 8, 4]
N = len(arr)
obj = MinHeap(arr)
# obj.heapsort()