// https://leetcode.com/problems/mirror-reflection

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        m,n = p,q
        while(m%2==0 and n%2 ==0):
            m=m//2
            n=n//2
        if m%2!=0 and n%2==0:return 0
        if m%2!=0 and n%2!=0: return 1
        if m%2==0 and n%2!=0:return 2
        return -1