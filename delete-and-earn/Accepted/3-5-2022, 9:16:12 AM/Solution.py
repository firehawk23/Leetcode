// https://leetcode.com/problems/delete-and-earn

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = [0]*(max(nums)+1)
        for i in nums:
            count[i] += i
        prev = count[0]
        curr = count[1]
        for i in range(2,len(count)):
            curr, prev = max(curr, prev + count[i]), curr
        return curr