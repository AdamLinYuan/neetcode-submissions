class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l,r = 0, len(s1) - 1
        count1 = Counter(s1)
        countW = Counter(s2[:len(s1)])

        while r < len(s2):
            if countW == count1:
                return True
            
            old_char = s2[l]
            countW[old_char] -= 1
            if countW[old_char] == 0:
                del countW[old_char]
        
            l += 1
            r += 1
            if r < len(s2):
                new_char = s2[r]
                countW[new_char] += 1
        return False