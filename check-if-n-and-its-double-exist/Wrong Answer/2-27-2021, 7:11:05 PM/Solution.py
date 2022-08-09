// https://leetcode.com/problems/check-if-n-and-its-double-exist

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i==2*j:
                    return True
        return False