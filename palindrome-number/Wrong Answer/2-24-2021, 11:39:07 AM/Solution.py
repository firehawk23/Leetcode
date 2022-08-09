// https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        if(a == a[::-1]):
            return 'true'
        return 'false'