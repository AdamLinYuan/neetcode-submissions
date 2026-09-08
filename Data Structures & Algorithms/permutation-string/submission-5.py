from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        # 1. Initialize logic
        l, r = 0, len(s1) - 1
        s1_count = Counter(s1)
        
        # Create the count for the FIRST window [0 : len(s1)-1]
        # We perform the slicing here just once to set up the baseline.
        window_count = Counter(s2[0 : len(s1)]) 

        # 2. Start your specific loop logic
        while r < len(s2):
            # Check if the current window matches
            if window_count == s1_count:
                return True
            
            # Prepare for the NEXT iteration (Slide the window)
            
            # A. Remove the character at 'l' (it's leaving the window)
            start_char = s2[l]
            window_count[start_char] -= 1
            if window_count[start_char] == 0:
                del window_count[start_char] # Critical: Remove key if 0
            
            # B. Move pointers
            l += 1
            r += 1
            
            # C. Add the character at the new 'r' (it's entering the window)
            if r < len(s2):
                end_char = s2[r]
                window_count[end_char] += 1
                
        return False