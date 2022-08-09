// https://leetcode.com/problems/sudoku-solver

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        n = 9
        def isValid(row, col, c):
            for i in range(9):
                if board[i][col] == c:
                    return False
                if board[row][i] == c:
                    return False
                if board[3*(row//3) + i//3][3*(col//3) + i%3] == c:
                    return False
            return True
            
        def solve(row, col):
            if row == n:
                return True
            if col == n:
                return solve(row+1, 0)
            
            if board[row][col] == ".":
                for c in range(1, 10):
                    if isValid(row, col, str(c)):
                        board[row][col] = str(c)
                        
                        if solve(row, col + 1):
                            return True
                        board[row][col] = "."
                return False
            else:
                return solve(row, col + 1)
            
        solve(0, 0)
		
