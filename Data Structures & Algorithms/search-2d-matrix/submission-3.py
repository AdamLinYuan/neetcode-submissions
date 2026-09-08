class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        index = -1
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:
                return self.search(matrix[i], target)
        return False
        

        
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        while l<=r:
            m = l + ((r-l)//2)
            if target == nums[m]:
                return True
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        
        return False