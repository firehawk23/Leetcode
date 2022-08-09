// https://leetcode.com/problems/remove-covered-intervals

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        l,r = len(intervals),0
        s = sorted(intervals,key = lambda i : (i[0],-i[1]))
        for e,i in s:
            if i<=r:
                l=l-1
            else:
                r = i
        return l