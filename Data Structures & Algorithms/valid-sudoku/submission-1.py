class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = [set() for _ in range(9)]
        c = [set() for _ in range(9)]
        b = [set() for _ in range(9)]
        for r1 in range(9):
            for c1 in range(9):
                num = board[r1][c1]
                if num=='.':
                    continue 
                box = r1//3 *3 +c1//3
                if num in r[r1] or num in c[c1] or num in b[box]:
                    return False
                r[r1].add(num)
                c[c1].add(num)
                b[box].add(num) 
        return True
                