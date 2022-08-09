// https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        for s in strs:
            t = tuple(sorted(s))
            if t not in table:
                table[t] = []
            table[t].append(s)
            
        res = []
        for t in table:
            res.append(table[t])
            
        return res