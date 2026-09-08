class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        hashSet = set()
        currMax = 0
        
        for r in range(len(s)):
            # If we found a duplicate, shrink window from the LEFT
            # until the duplicate is removed from the set
            while s[r] in hashSet:
                hashSet.remove(s[l]) # Remove the character at left pointer
                l += 1               # Move left pointer forward
            
            # Now it's safe to add the new character
            hashSet.add(s[r])
            
            # Update max (Window size is r - l + 1)
            currMax = max(currMax, r - l + 1)
        
        return currMax