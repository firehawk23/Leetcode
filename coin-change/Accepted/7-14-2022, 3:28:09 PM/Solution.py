// https://leetcode.com/problems/coin-change

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = float('inf')
        t = [0 for i in range(amount+1)]
        for i in range(1,amount+1):
            t[i] = min([t[i - c] if i - c >= 0 else MAX for c in coins]) + 1

        return [t[amount], -1][t[amount] == MAX]