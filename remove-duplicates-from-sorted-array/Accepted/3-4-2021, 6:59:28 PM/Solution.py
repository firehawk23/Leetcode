// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-1,0,-1):
            if nums[i] == nums[i-1]:
                nums.remove(nums[i])
        return len(nums)