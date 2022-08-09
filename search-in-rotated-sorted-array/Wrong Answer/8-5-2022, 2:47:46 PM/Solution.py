// https://leetcode.com/problems/search-in-rotated-sorted-array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while(l<r):
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                 l= mid+1
            else:
                r= mid-1
        rot = l
        l,r=0,len(nums)-1
        while(l<=r):
            mid = (l+r)//2
            real_m = (mid+rot)%len(nums)
            if nums[real_m] == target:
                return real_m
            if nums[real_m]<target:
                l = mid +1
            else:
                r= mid-1
        
        return -1