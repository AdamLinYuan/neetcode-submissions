from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minK, maxK = 1, max(piles)
        res = maxK

        while minK <= maxK:
            mid = minK + (maxK - minK)//2
            totalTime = 0

            for pile in piles:
                totalTime += ceil(pile / mid)

            if totalTime <= h:
                res = mid
                maxK = mid - 1
            else:
                minK = mid + 1

        return res
        