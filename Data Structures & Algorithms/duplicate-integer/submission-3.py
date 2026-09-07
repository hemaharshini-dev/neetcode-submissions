class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_duplicate = set()
        for num in nums:
            if num in no_duplicate:
                return True
            no_duplicate.add(num)
        return False