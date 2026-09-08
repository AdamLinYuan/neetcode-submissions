class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortNums = sorted(nums)
        n = len(nums)
        res = []
        for i in range(n):
            if i>0 and sortNums[i] == sortNums[i-1]:
                continue
            l, r = i + 1, n - 1
            target = -sortNums[i]
            while l < r:
                if sortNums[l] + sortNums[r] == target:
                    res.append([sortNums[i], sortNums[l], sortNums[r]])
                    l += 1
                    r -= 1
                    while l < r and sortNums[l] == sortNums[l-1]:
                        l += 1
                elif sortNums[l] + sortNums[r] <= target:
                    l += 1
                elif sortNums[l] + sortNums[r] >= target:
                    r -= 1
        
        return res