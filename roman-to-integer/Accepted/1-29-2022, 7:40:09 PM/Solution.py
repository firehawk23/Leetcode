// https://leetcode.com/problems/roman-to-integer

d ={"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
d2 ={"IV": 4,"IX": 9,"XL": 40, "XC": 90,"CD": 400,"CM": 900}

class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        while s != "":
            if len(s) == 1:
                total += d[s]
                s = ""
            elif s[:2] in d2:
                total += d2[s[:2]]
                s = s[2:]
            else:
                total += d[s[0]]
                s = s[1:]
        return total