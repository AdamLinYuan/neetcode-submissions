class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        smallest = min(strs) or strs[0]

        if "" in strs:
            return res
        for i in range(len(smallest)):
            for word in strs:
                if word[i] != smallest[i]:
                    return res
            res += smallest[i]

        return res