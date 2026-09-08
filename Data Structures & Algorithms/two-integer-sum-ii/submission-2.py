# HashMap

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = defaultdict(int)
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in mp:
                return [mp[diff] + 1, i + 1]
            mp[num] = i