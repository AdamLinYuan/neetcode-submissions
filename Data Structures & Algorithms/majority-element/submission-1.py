class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = Counter()
        res = maxCount = 0
        for num in nums:
            hashmap[num] += 1
            if maxCount < hashmap[num]:
                res = num
                maxCount = hashmap[num]

        return res