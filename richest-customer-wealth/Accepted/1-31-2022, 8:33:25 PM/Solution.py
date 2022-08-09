// https://leetcode.com/problems/richest-customer-wealth

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        a =0
        for i in accounts:
            total = sum(i)
            a = max(a,total)
        return a