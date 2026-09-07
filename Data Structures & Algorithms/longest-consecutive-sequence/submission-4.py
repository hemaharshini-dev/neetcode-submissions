class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        long = 1
        l = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]+1:
                l+=1
            elif nums[i]==nums[i-1]:
                continue
            else:
                l=1

            long = max(long,l)
        return long
        
            
