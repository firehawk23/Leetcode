// https://leetcode.com/problems/sort-array-by-parity

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        for i in range(len(A)):
            if(A[i]%2 != 0):
                A.append(A[i])
                A.remove(A[i])
        return A