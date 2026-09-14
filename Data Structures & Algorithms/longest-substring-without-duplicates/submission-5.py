class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = {}
        l, res = 0, 0
        for r in range(len(s)):
            if s[r] in hashMap:
                l = max(hashMap[s[r]] + 1, l)
            hashMap[s[r]] = r
            res = max(r - l + 1, res)
        return res
