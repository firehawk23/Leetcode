// https://leetcode.com/problems/height-checker

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        result = 0
        c_order = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != c_order[i]:
                result += 1
        return result