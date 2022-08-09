// https://leetcode.com/problems/reverse-integer

class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        s = 1
        if (x<0):
            x *= -1
            s = -1
        while(x>0):
            temp = x%10
            rev = rev*10 + temp
            x = x//10
        if rev < -2147483648 or rev > 2147483647:
            return 0
        return rev*s