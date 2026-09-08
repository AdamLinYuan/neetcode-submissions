class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        def dfs(i):
            if sum(subset) == target:
                if subset in res:
                    return
                res.append(subset.copy())
                return
            if i >= len(candidates) or sum(subset) > target:
                return

            subset.append(candidates[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res