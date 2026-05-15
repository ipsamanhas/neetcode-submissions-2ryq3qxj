class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
         # each subarray stores the row
         # will have 9 diff subarrays
         # each subarray will have 9 elements -> len(subarray) = 9

         # each row, col and square will have nums 0-9 distinctively
         # we can have a hashset to check for duplicates
         rows = collections.defaultdict(set)
         cols = collections.defaultdict(set)
         square = collections.defaultdict(set)

         for r in range(9):
            for c in range(9):
                if board[r][c] == ".":  # skip empty cells
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in square[(r//3, c//3)]):
                    return False
                
                # add the vals to the set 
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                square[r//3, c//3].add(board[r][c])

         return True

                

