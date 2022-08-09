// https://leetcode.com/problems/combination-sum-iv

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        t = [0 for i in range(target+1)]
        for i in nums:
            if i<=target:
                t[i] = 1
        for i in range(1,target+1):
            for j in nums:
                if i-j>0:
                    t[i] += t[i-j]
                    
        return t[-1]