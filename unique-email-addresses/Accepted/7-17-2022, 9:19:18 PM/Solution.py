// https://leetcode.com/problems/unique-email-addresses

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        d = dict()
        for i in emails:
            l = i.split("@")
            tmp = l[0].split("+")
            l[0] = tmp[0]
            tmp1 = l[0].split(".")
            l[0] = "".join(tmp1)
            g = "@".join(l)
            if g not in d:
                d[g] = 1
            else:
                d[g]+=1
        return len(d)