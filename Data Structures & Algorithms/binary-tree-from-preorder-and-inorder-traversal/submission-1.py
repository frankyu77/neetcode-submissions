# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indexes = {val: i for i, val in enumerate(inorder)}
        pre_idx = 0

        def recurse(lo, hi):
            nonlocal pre_idx
            if lo > hi:
                return None

            value = preorder[pre_idx]
            index = indexes[value]
            pre_idx += 1

            left_child = recurse(lo, index - 1)
            right_child = recurse(index + 1, hi)

            return TreeNode(value, left_child, right_child)

        return recurse(0, len(inorder) - 1)