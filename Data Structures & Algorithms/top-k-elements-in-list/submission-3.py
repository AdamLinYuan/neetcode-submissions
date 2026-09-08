#Bucket Sort Version
from collections import Counter
import itertools

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]
        count = Counter(nums)

        for num, freq in count.items():
            bucket[freq].append(num)

        res = []
        for freq in range(len(bucket) - 1, 0, -1):
            for n in bucket[freq]:
                res.append(n)
                if len(res) == k:
                    return res