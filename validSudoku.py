from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        #defines set hashes
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)
        #scan through board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                #ignore blanks
                if num == ".":
                    continue
                #if repeated number in each row, col or square ret false
                if(
                    num in row[i] or 
                    num in col[j] or
                    num in square[(i//3, j//3)]):
                    return False
                #for each hash add current number
                row[i].add(num)
                col[j].add(num)
                square[(i//3, j//3)].add(num)
        #if no false then true
        return True

        