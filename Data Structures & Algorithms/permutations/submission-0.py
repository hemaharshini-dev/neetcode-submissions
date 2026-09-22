class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def recurPermute(index):
            if index == len(nums):
                ans.append(nums[:])
                return
            
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                recurPermute(index + 1)
                nums[index], nums[i] = nums[i], nums[index]
        
        ans = []
        recurPermute(0)
        return ans