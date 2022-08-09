// https://leetcode.com/problems/contiguous-array

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len =0
        curr_max_len = 0
        d={0:-1}
        for i,num in enumerate(nums):
            if num==1:
                curr_max_len+=1
            else:
                curr_max_len-=1
            if curr_max_len in d:
                max_len = max(max_len,i-d[curr_max_len])
            else:
                d[curr_max_len]=i
        return max_len
                