class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1. Find the Pivot (Minimum element) - Your code was correct here!
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        
        pivot = l  # This is the index of the smallest number
        
        # 2. Decide which side to search
        # Don't slice! Just set l and r to the correct range.
        if target >= nums[pivot] and target <= nums[-1]:
            # Target is in the right sorted portion (e.g., [0, 1, 2])
            l = pivot
            r = len(nums) - 1
        else:
            # Target is in the left sorted portion (e.g., [4, 5, 6, 7])
            l = 0
            r = pivot - 1
            
        # 3. Standard Binary Search
        while l <= r:  # CHANGED: 'while', not 'if'
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
                
        return -1