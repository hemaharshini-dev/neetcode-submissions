class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                for j in range(9):
                    if j!=c and board[r][j] == board[r][c]:
                        return False

                for i in range(9):
                    if i!=r and board[i][c] == board[r][c]:
                        return False

                br = (r//3)*3
                bc = (c//3)*3
                for i in range(br,br+3):
                    for j in range(bc,bc+3):
                        if (i!=r or j!=c) and board[i][j]==board[r][c]:
                            return False 
        return True