class Solver:
    def solveSudoku(self, board) -> None:
        found = self.findEmpty(board)
        if not found:
            return True
        r, c = found
        
        # backtracking algorithm
        for num in range(1, 10):
            if self.valid(board, r, c, str(num)):
                board[r][c] = str(num)
                if self.solveSudoku(board):
                    return board
                board[r][c] = '.'
        return False
                
                
    # returns an empty slot
    def findEmpty(self, board) -> List:
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    return (r, c)
        
        return None
    
    
    # checks whether the given number is valid
    def valid(self, board, r, c, num) -> bool:
        # validates the column
        for currRow in range(9):
            if board[currRow][c] == num and currRow != r:
                return False
        
        # validates the row
        for currCol in range(9):
            if board[r][currCol] == num and currCol != c:
                return False
        
        # validates the 3x3 square
        squareX = c // 3
        squareY = r // 3
        for currRow in range(squareY*3, squareY*3 + 3):
            for currCol in range(squareX*3, squareX*3 + 3):
                if board[currRow][currCol] == num and (currRow, currCol) != (r, c):
                    return False
        
        return True
