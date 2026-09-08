from heapq import heapify, heappush, heappop, heappushpop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        while len(nums) > k:
            heappop(nums)
        return nums[0]