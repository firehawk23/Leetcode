// https://leetcode.com/problems/transpose-matrix

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        List=[]  
        for i in range(len(matrix[0])):
            List.append([])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                List[j].append(matrix[i][j])
        return List