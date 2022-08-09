// https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(arr,path,res):
            if not arr:
                res.append(path)
                return
            for i,n in enumerate(arr):
                dfs(arr[:i]+arr[i+1:],path+[n],res)
        res =[]
        dfs(nums,[],res)
        return res