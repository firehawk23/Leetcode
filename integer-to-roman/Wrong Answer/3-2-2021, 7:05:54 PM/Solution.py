// https://leetcode.com/problems/integer-to-roman

class Solution:
    def intToRoman(self, num: int) -> str:
        n = [1,5,10,50,100,500,1000]
        r = ['I','V','X','L','C','D','M']
        i = 6
        a =''
        while(num):
            d = num//n[i]
            num = num % n[i]
            while(d):
                a = a+r[i]
                d=d-1
            i=i-1
        return a
        