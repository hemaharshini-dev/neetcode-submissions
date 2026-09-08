class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        o = [1]*len(nums)
        for i in range(len(nums)):
            o[i] = p
            p*=nums[i]

        s = 1
        for i in range(len(nums)-1,-1,-1):
            o[i]*=s
            s*=nums[i]
        return o