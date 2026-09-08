import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [[] for i in nums]
        for i, num in enumerate(nums):
            output[i] = int(math.prod(nums[:i] + nums[i+1:]))

        return output