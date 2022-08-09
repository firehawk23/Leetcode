// https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcps = ""
        for i in range(min(list(map(lambda x : len(x), strs)))):
            char = strs[0][i]
            for j in strs:
                if(j[i]!=char):
                    return lcps
            lcps = lcps+char
        return lcps