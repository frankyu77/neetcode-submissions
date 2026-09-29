# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0

        def maxDepth(node):
            nonlocal best
            if node is None:
                return 0
            
            leftSubTree = maxDepth(node.left)
            rightSubTree = maxDepth(node.right)

            best = max(best, leftSubTree + rightSubTree)
            return 1 + max(leftSubTree, rightSubTree)
        
        maxDepth(root)
        return best