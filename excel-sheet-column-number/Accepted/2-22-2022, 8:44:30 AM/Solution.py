// https://leetcode.com/problems/excel-sheet-column-number

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        sol = 0
        for i in columnTitle:
            d = ord(i)-ord('A')+1
            sol = sol*26+d
        return sol