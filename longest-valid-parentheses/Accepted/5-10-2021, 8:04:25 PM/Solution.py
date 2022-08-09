// https://leetcode.com/problems/longest-valid-parentheses

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        stk = [-1]
        res = 0
        for i in range(n):
            if s[i]=='(':
                stk.append(i)
            else:
                stk.pop()
                if len(stk)!=0:
                    res = max(res,i-stk[-1])
                else:
                    stk.append(i)
        return res