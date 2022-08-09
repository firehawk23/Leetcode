// https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def letterCombinations(self, digits):
        d = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7': "pqrs", '8':"tuv", '9':"wxyz"}
        cmb = [''] if digits else []
        for i in digits:
            cmb = [p + q for p in cmb for q in d[i]]
        return cmb
    