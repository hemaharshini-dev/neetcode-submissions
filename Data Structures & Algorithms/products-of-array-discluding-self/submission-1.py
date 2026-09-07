class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        n = len(nums)
        ans = [1]*n
        for i in range(n):
            ans[i] = p
            p*=nums[i]

        s = 1
        for j in range(n-1,-1,-1):
            ans[j]*= s
            s*=nums[j]
        return ans