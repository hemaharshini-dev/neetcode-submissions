class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns = set(nums)
        l = 0
        for num in nums:
            if num-1 in ns:
                continue
            c = 1
            while num+c in ns:
                c+=1
            l = max(c,l)
        return l

