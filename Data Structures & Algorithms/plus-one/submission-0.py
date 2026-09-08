class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = ""
        for d in digits:
            res += str(d)

        res = str(int(res) + 1)
        arr = []
        for d in res:
            arr.append(int(d))
        return arr

