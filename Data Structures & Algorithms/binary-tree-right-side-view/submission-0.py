from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        sol = []

        if root is None:
            return sol
        
        q.append(root)

        while q:
            right_most = q.popleft()
            sol.append(right_most.val)

            size = len(q)

            if right_most.right:
                q.append(right_most.right)
            if right_most.left:
                q.append(right_most.left)

            for _ in range(size):
                node = q.popleft()
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        return sol

