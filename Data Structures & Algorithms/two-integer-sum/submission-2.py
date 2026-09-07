class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i,num in enumerate(nums):
            c = target-nums[i]
            if c in h:
                return [h[c], i]
            h[num] = i