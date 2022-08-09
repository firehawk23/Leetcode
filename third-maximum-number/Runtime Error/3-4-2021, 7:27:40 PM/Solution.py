// https://leetcode.com/problems/third-maximum-number

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        t=2
        while(t--):
            num.remove(max(nums))
        return max(nums)