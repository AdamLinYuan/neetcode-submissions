from heapq import heapify, heappush, heappop, heappushpop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [n * -1 for n in stones]
        heapify(maxHeap)

        while len(maxHeap) > 1:
            x = heappop(maxHeap) * -1
            y = heappop(maxHeap) * -1
            if x == y:
                pass
            newStone = max(x,y) - min(x,y)
            heappush(maxHeap, newStone * -1)
        return maxHeap[0] * -1
        