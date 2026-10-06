class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol, path = [], []

        def dfs(i):
            if i == len(nums):
                sol.append(path[:])
                return
            
            # add the current number
            path.append(nums[i])
            dfs(i+1)
        
            # dont add the current number
            path.pop()
            dfs(i+1)
        dfs(0)
        return sol