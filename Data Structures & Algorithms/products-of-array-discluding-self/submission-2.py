class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zeros = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zeros += 1
        
        res = [0] * len(nums)

        if zeros > 1:
            return res
        
        
        for i, num in enumerate(nums):
            if zeros:
                if num == 0:
                    res[i] = prod
            else:
                res[i] = prod // num

        return res