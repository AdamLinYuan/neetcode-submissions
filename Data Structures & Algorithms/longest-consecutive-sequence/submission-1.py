

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(set(nums))
        temp = 1
        ctr = 0

        for i in range(1,len(nums)):
            if (nums[i-1] + 1) == nums[i]:
                temp += 1
            else:
                ctr = max(temp, ctr)
                temp = 1

        ctr = max(temp, ctr)

        return ctr
                
        