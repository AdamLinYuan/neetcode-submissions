class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set(nums)
        if len(nums) == len(hashSet):
            return False
        return True
