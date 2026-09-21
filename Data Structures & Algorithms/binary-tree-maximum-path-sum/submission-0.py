# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -math.inf
        def maxPathDown(root):
            if not root:
                return 0
            nonlocal ans
            l = max(0, maxPathDown(root.left))
            r = max(0,maxPathDown(root.right))
            ans = max(ans, root.val+l+r)
            return root.val+max(l,r)
        maxPathDown(root)
        return ans