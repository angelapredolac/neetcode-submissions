class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board:
            return True
        
        row_to_vals = {row: set() for row in range(len(board))}
        col_to_vals = {col: set() for col in range(len(board[0]))}
        box_to_vals = {}

        for row in range(len(board)):
            for col in range(len(board[0])):
                val = board[row][col]
                if val==".":
                    continue
                elif not val.isdigit() or int(val)<1 or int(val)>9:
                    return False
                box = (row//3, col//3)
                if box not in box_to_vals.keys():
                    box_to_vals[box] = set()
                if val in row_to_vals[row] or val in col_to_vals[col] or val in box_to_vals[box]: 
                    return False
                row_to_vals[row].add(val)
                col_to_vals[col].add(val)
                box_to_vals[box].add(val)
        
        return True