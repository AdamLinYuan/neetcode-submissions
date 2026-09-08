class Solution:
    def productExceptSelf(self,  nums: List[int]) -> List[int]:
        prod, zeroCntr = 1,0
        for n in nums:
            if n:
                prod *= n
            else:
                zeroCntr += 1

        if zeroCntr >1 :
            return [0] * len(nums)
        res = [0] * len(nums)
        for i,n in enumerate(nums):
            if zeroCntr:
                if n:
                    res[i] = 0
                else:
                    res[i] = prod
            else:
                res[i] = prod//n

        return res