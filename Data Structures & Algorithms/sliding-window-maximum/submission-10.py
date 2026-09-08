class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        # if len(nums) < k:
        #     return res


        currArr = nums[:k]
        currMax = max(currArr)
        res.append(currMax)
        for i in range(k, len(nums)):
            currArr.append(nums[i])
            currArr.pop(0)
            currMax = max(currArr)
            res.append(currMax)
        return res