// https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        l_max=0
        r_max=0
        res =0
        while(l<=r):
            if r_max<l_max:
                res += max(0,r_max-height[r])
                r_max = max(r_max,height[r])
                r = r-1
            else:
                res += max(0,l_max-height[l])
                l_max = max(l_max,height[l])
                l = l+1
        return res