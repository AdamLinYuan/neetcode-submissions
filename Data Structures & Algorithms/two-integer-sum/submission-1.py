class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashSet = {val: i for i, val in enumerate(nums)}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashSet and hashSet[diff] != i:
                return [i, hashSet[diff]]

            

