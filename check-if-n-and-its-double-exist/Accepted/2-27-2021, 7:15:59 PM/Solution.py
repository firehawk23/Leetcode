// https://leetcode.com/problems/check-if-n-and-its-double-exist

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        return arr.count(0)>1 or any(2* x in set(arr) for x in set(arr) if x)