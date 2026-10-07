class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        sol, rsf = [], []

        def dfs(i, total):
            if total == target:
                sol.append(rsf[:])
                return
            if total > target or i >= len(candidates):
                return
            
            rsf.append(candidates[i])
            dfs(i + 1, total + candidates[i])

            rsf.pop()
            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            dfs(j, total)
        dfs(0, 0)
        return sol