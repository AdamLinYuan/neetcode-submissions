from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minK, maxK = 1, max(piles)
        res = maxK
        
        while minK <= maxK:
            mid = minK + (maxK - minK)//2
            summ = 0

            for x in piles:
                summ += ceil(x/mid)

            if summ <= h:
                res = mid
                maxK = mid - 1
            else:
                minK = mid + 1
        return res
                