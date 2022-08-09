// https://leetcode.com/problems/jewels-and-stones

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d = dict()
        count =0
        for i in range(len(jewels)):
            d[jewels[i]] = 0
        for i in range(len(stones)):
            if stones[i] in d:
                d[stones[i]] += 1
        for i in range(len(d)):
            count += d[jewels[i]]
        return count
                