# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        dq = collections.deque([root])
        while dq:
            cl = []
            for _ in range(len(dq)):
                q = dq.popleft()
                cl.append(q.val)
                if q.left:
                    dq.append(q.left)
                if q.right:
                    dq.append(q.right)
            ans.append(cl)
        return ans