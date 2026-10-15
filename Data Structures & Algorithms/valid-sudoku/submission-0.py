class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. traverse rows
        dim = 9
        for i in range(dim):
            row_set = set()
            current_row = board[i]
            for r in current_row:
                if r != "." and r in row_set:
                    return False
                else:
                    row_set.add(r)

        # 2. traverse cols
        for i in range(dim):
            col_set = set()
            current_col = [col[i] for col in board]
            for c in current_col:
                if c != "." and c in col_set:
                    return False
                else:
                    col_set.add(c)

        # 3. traverse sub-boxes
        boxes = {
            (0, 0): [],
            (0, 1): [],
            (0, 2): [],
            (1, 0): [],
            (1, 1): [],
            (1, 2): [],
            (2, 0): [],
            (2, 1): [],
            (2, 2): [],
        }
        for i in range(dim):
            for j in range(dim):
                square = board[i][j]
                key = (i // 3, j // 3)
                print(f"i: {i}, j: {j}, key: {key}, value: {square}")
                if square != ".":
                    if key in boxes and square not in boxes[key]:
                        boxes[key].append(square)
                    else:
                        return False
        return True

