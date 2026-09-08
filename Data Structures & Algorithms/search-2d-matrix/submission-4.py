class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l,r = 0, (rows * cols - 1)

        while l<=r:
            m = l + (r-l)//2

            mVal = matrix[m//cols][m%cols]
            print(mVal)

            if mVal == target:
                return True
            elif mVal < target:
                l = m+1
            else: 
                r = m-1
            
        return False