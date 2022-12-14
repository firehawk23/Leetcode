// https://leetcode.com/problems/valid-sudoku

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #checking if 1D array valid
        def valid(arr):
            seen = set()
            for val in arr:
                if val == '.':
                    continue
                if val in seen:
                    return False
                seen.add(val)
            return True
        
        #Row wise
        for row in board:
            if not valid(row):
                return False
        
        #column wise
        for j in range(9):
            col = [board[i][j] for i in range(9)]
            if not valid(col):
                return False
       #Block wise
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                block = [board[k][l] for k in range(i, i+3) for l in range(j, j+3)]
                if not valid(block):
                    return False
        return True