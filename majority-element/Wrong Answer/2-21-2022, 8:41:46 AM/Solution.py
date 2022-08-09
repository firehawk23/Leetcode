// https://leetcode.com/problems/majority-element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = dict()
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] = d[i]+1
        
        for key in d:
            if d[key]>= len(nums)//2:
                return key