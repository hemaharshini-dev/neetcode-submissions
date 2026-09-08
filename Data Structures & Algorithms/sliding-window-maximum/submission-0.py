from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        op = []
        n = len(nums)
        for i in range(n):
            if dq and dq[0]<i+1-k:  #left
                dq.popleft()
            while dq and nums[dq[-1]]<nums[i]:
                dq.pop()
            dq.append(i)
            if i>=k-1:
                op.append(nums[dq[0]])
        return op

        