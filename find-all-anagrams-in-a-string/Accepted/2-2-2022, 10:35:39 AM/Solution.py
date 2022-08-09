// https://leetcode.com/problems/find-all-anagrams-in-a-string

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = list()
        temp = list(p)
        st = 0
        for i in range(len(s)):
            if s[i] not in p:
                temp = list(p)
                st = i+1
            else:
                if s[i] in temp:
                    temp.remove(s[i])
                else:
                    while(s[st]!=s[i]):
                        temp.append(s[st])
                        st+=1
                    st+=1
            if temp==[]:
                res.append(st)
        return res