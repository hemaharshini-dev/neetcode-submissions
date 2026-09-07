class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        mini = prices[0]
        n = len(prices)
        for i in range(n):
            mp = max(mp,prices[i]-mini)
            mini = min(mini,prices[i])
        return mp