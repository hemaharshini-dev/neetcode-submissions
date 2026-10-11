class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        buying = [0] * (n + 2)
        holding = [0] * (n + 2)

        for i in range(n - 1, -1, -1):
            buying[i] = max(
                -prices[i] + holding[i + 1],
                buying[i + 1]
            )

            holding[i] = max(
                prices[i] + buying[i + 2],
                holding[i + 1]
            )

        return buying[0]