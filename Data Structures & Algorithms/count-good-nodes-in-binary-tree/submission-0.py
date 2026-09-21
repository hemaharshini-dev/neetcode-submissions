# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root,max_):
            if not root:
                return 0
            good = 1 if root.val>=max_ else 0
            max_ = max(max_,root.val)
            return good+dfs(root.right,max_)+dfs(root.left,max_)
        return dfs(root,root.val)