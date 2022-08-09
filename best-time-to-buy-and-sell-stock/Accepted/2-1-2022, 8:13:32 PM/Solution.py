// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp = 999999999
        bp = 0
        for i in prices:
            profit = i-lp
            bp = max(profit,bp)
            lp = min(i,lp)
        return bp