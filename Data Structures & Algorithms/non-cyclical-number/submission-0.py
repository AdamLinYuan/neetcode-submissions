class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        # We loop until we find 1
        while n != 1:
            # FIX 1: Check if the CURRENT number (n) has been seen to detect cycles
            if n in seen:
                return False
            seen.add(n)

            # FIX 2: Create the array for the CURRENT 'n' (not the old one)
            nstr = str(n)
            arr = [int(d) for d in nstr]

            # FIX 3: Reset 'res' to 0 for this new calculation
            res = 0
            
            # Your logic of iterating through the array (simplified with a for-loop)
            for d in arr:
                res += d ** 2
            
            # FIX 4: Update n to be the result we just calculated
            n = res
            
        return True