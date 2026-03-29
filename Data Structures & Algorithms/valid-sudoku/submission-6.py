class Solution:

    from collections import defaultdict

    def isValidSudoku(self, board: List[List[str]]) -> bool:


        checkRows = defaultdict(set)
        checkCols = defaultdict(set)
        squares = defaultdict(set)

        if len(board) < 9:
            return False
        



        for i in range(9):
            for j in range(9):          
                if board[i][j] == ".":
                    continue

                if (board[i][j] in checkRows[i] or 
                    board[i][j] in checkCols[j] or
                    board[i][j] in squares[(i//3,j//3)]):
                    return False
                
                checkCols[j].add(board[i][j])
                checkRows[i].add(board[i][j])
                squares[(i//3,j//3)].add(board[i][j])

        return True





        