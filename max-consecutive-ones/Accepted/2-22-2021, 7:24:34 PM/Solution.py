// https://leetcode.com/problems/max-consecutive-ones

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt =0
        sum1= 0
        prev =0
        for i in range(len(nums)):
            prev = max(cnt,prev)
            if nums[i]==1:
                cnt+=1
            if nums[i]==0:
                cnt=0
            sum1 = max(cnt,prev)
        return sum1