from heapq import heapify, heappush, heappop, heappushpop
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for pt in points:
            dist = pt[0]**2 + pt[1]**2
            distance.append((dist, pt))

        heapify(distance)
        res = []

        for _ in range(k):
            closest_point = heappop(distance)[1]
            res.append(closest_point)

        return res