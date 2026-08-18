class Heap:
    def __init__(self) -> None:
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def l_child(self, i):
        return (2 * i) + 1

    def r_child(self, i):
        return (2 * i) + 2

    def add(self, num):
        self.heap.append(num)
        self.up_heapify(len(self.heap) - 1)

    def extract(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        min_element = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.down_heapify(0)
        return min_element

    def up_heapify(self, i):
        current = i
        while current != 0 and self.heap[self.parent(current)] > self.heap[current]:
            self.heap[self.parent(current)], self.heap[current] = (
                self.heap[current],
                self.heap[self.parent(current)],
            )
            current = self.parent(current)

    def down_heapify(self, i):
        smallest = i
        left = self.l_child(i)
        right = self.r_child(i)
        heap_size = len(self.heap)

        if left < heap_size and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < heap_size and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]
            self.down_heapify(smallest)


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # make a heap with the nums, extract min until length of heap <=k
        self.heap = Heap()
        self.k = k
        for num in nums:
            self.heap.add(num)
        
        while len(self.heap.heap) > k:
            self.heap.extract()


    def add(self, val: int) -> int:
        self.heap.add(val)
        while len(self.heap.heap) > self.k:
            self.heap.extract()
        return self.heap.heap[0]
        
        
