from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for count in freq.values():
            if count > 1:
                return True 
        return False