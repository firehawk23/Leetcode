// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a = []
        n= max(nums)+1
        for i in range(1,n):
            if i not in nums:
                a.append(i)
        return a
            