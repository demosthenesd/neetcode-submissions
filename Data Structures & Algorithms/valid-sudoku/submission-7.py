class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        from collections import defaultdict

        checkRows = defaultdict(set)
        checkCols = defaultdict(set)
        smallGrid = defaultdict(set)
        

        for row in range(9):
            for col in range(9):

                if(board[row][col] == "."):
                    continue
                
                if(
                    board[row][col] in checkRows[row] or
                    board[row][col] in checkCols[col] or
                    board[row][col] in smallGrid[(row//3,col//3)]
                    ):
                    return False
                
                checkRows[row].add(board[row][col])
                checkCols[col].add(board[row][col])
                smallGrid[(row//3,col//3)].add(board[row][col])
        
        return True











