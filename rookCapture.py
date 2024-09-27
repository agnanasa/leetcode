class Solution:
    def numRookCaptures(self, board):
        # Find the position of the rook (R)
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rook_row, rook_col = i, j
                    break

        captures = 0

        # Check upwards (towards row 0)
        for row in range(rook_row - 1, -1, -1):
            if board[row][rook_col] == 'B':  # Blocked by a bishop
                break
            if board[row][rook_col] == 'p':  # Pawn found
                captures += 1
                break

        # Check downwards (towards row 7)
        for row in range(rook_row + 1, 8):
            if board[row][rook_col] == 'B':  # Blocked by a bishop
                break
            if board[row][rook_col] == 'p':  # Pawn found
                captures += 1
                break

        # Check left (towards column 0)
        for col in range(rook_col - 1, -1, -1):
            if board[rook_row][col] == 'B':  # Blocked by a bishop
                break
            if board[rook_row][col] == 'p':  # Pawn found
                captures += 1
                break

        # Check right (towards column 7)
        for col in range(rook_col + 1, 8):
            if board[rook_row][col] == 'B':  # Blocked by a bishop
                break
            if board[rook_row][col] == 'p':  # Pawn found
                captures += 1
                break

        return captures

# Example usage
board = [[".",".",".",".",".",".",".","."],
         [".",".",".","p",".",".",".","."],
         [".",".",".","R",".",".",".","p"],
         [".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".","."],
         [".",".",".","p",".",".",".","."],
         [".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".","."]]

solution = Solution()
print(solution.numRookCaptures(board))  # This will work
