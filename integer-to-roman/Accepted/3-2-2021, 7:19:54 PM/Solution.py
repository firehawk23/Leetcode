// https://leetcode.com/problems/integer-to-roman

class Solution:
    def intToRoman(self, num: int) -> str:
        n = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        r = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        i = 12
        a =''
        while(num):
            d = num//n[i]
            num = num % n[i]
            while(d):
                a = a+r[i]
                d=d-1
            i=i-1
        return a
        