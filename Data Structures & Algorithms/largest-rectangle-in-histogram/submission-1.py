class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        maxArea = 0
        for i in range(n):
            minHeight = heights[i]
            for j in range(i, n):
                minHeight = min(minHeight, heights[j])
                maxArea = max(maxArea, minHeight * (j - i + 1))
                
                
        return maxArea