// https://leetcode.com/problems/game-of-life

class Solution:
    def withinBoundry(self, m: int, n: int, row: int, col: int) -> bool:
        return (0 <= row < m) and (0 <= col < n)

    def findNeighbours(self,board:List[List[int]],m:int,n:int,row:int,col:int) -> int:
        num_neigh = 0
        directions = [(row-1, col-1), (row, col-1), (row+1, col-1),
                      (row-1, col), (row+1, col),
                      (row-1, col+1), (row, col+1), (row+1, col+1)]
        for dir in directions:
            if self.withinBoundry(m,n,dir[0],dir[1]):
                num_neigh = num_neigh+board[dir[0]][dir[1]]
        return num_neigh
        
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)
        n = len(board[0])
        neighbours = [[0 for j in range(n)] for i in range(m)]
        for row in range(m):
            for col in range(n):
                neighbours[row][col] = self.findNeighbours(board,m,n,row,col)
        for row in range(m):
            for col in range(n):
                if board[row][col]==1 and neighbours[row][col]<2:
                    board[row][col]=0
                elif board[row][col]==1 and neighbours[row][col]>3:
                    board[row][col]=0
                elif board[row][col]==1 and (2<=neighbours[row][col]<=3):
                    board[row][col]=1
                elif board[row][col]==0 and neighbours[row][col]==3:
                    board[row][col]=1
                else:
                    pass
        return