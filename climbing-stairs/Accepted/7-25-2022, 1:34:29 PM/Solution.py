// https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        t = [0]*(n+1)
        t[0] = 1
        t[1] = 1
        for i in range(2,n+1):
            t[i] = t[i-1]+t[i-2]
        
        
        return t[n]