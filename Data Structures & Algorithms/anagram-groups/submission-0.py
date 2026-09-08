from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for string in strs:
            sortedString = ''.join(sorted(string))
            hashMap[sortedString].append(string)
        return list(hashMap.values())