from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1

        sortByFreq = sorted(counter, key = counter.get, reverse = True)
        return sortByFreq[0:k]