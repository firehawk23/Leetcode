// https://leetcode.com/problems/running-sum-of-1d-array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = nums[0]
        for i in range(1,len(nums)):
            nums[i] = nums[i]+sum
            sum = nums[i]
        return nums