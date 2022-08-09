// https://leetcode.com/problems/unique-paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def fact(x):
            if x == 1:
                return 1
            return x*fact(x-1)
        
        ans = fact(m+n-2)//(fact(n-1)*fact(m+n-2-n+1))
        return ans