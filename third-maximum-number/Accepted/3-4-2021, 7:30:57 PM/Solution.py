// https://leetcode.com/problems/third-maximum-number

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a = set(nums)
        m = max(a)
        if len(a) > 2:
            i = 3
            while i > 1:
                a.remove(m)
                m = max(a)
                i -= 1
        return m