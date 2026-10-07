class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob_linear(nums):
            prev = nums[0]
            prev2 = 0

            for i in range(1, len(nums)):
                take = nums[i] + prev2
                notTake = prev

                curr = max(take, notTake)

                prev2 = prev
                prev = curr

            return prev

        if len(nums) == 1:
            return nums[0]

        case1 = rob_linear(nums[:-1])

        case2 = rob_linear(nums[1:])

        return max(case1, case2)