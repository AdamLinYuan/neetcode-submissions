from heapq import heapify, heappush, heappop, heappushpop

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapify(self.minHeap)
        
        # Keep only the K largest elements
        # (By popping the smallest ones until size is k)
        while len(self.minHeap) > k:
            heappop(self.minHeap)

    def add(self, val: int) -> int:
        # If heap isn't full yet, just push
        if len(self.minHeap) < self.k:
            heappush(self.minHeap, val)
        # If new val is larger than the smallest in heap, replace it
        elif val > self.minHeap[0]:
            heappushpop(self.minHeap, val)
            
        # The root of the Min-Heap is the K-th largest element
        return self.minHeap[0]