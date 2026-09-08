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
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]