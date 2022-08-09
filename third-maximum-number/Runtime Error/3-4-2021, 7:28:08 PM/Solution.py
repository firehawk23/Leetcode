// https://leetcode.com/problems/third-maximum-number

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        t=2
        while(t!=0):
            num.remove(max(nums))
            t=t-1
        return max(nums)