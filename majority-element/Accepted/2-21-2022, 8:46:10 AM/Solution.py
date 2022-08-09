// https://leetcode.com/problems/majority-element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        x = list(d.items())
        x.sort(key=lambda x: x[1])
        return x[-1][0]