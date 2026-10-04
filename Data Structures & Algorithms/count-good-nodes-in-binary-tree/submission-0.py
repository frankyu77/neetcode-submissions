# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, msf):
            if not node:
                return 0
            good = 0
            if node.val >= msf:
                good = 1
            new_msf = max(node.val, msf)
            return good + dfs(node.left, new_msf) + dfs(node.right, new_msf)

        return dfs(root, root.val)