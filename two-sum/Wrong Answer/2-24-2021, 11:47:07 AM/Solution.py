// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n =len(nums)
        b=[]
        for i in range(n):
            for j in range(i,n):
                if(nums[i]+nums[j]==target):
                    b.append(i)
                    b.append(j)
                    return b