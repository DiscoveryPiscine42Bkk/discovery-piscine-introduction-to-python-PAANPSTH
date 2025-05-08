#!/usr/bin/env python3

def main():
    n = len(board)
    if n == 0 or n != c:
        return

    king_pos = None
    for r in range(n):
        for c in range(n):
            if board[r][c] == 'K':
                king_pos = (r, c)
                break
        if king_pos:
            break

    if not king_pos:
        return  # Handle case where King is not on the board

    king_r, king_c = king_pos

    # Check for Pawns
    pawn_attacks = [(king_r - 1, king_c - 1), (king_r - 1, king_c + 1)]
    for pr, pc in pawn_attacks:
        if 0 <= pr < n and 0 <= pc < n and board[pr][pc] == 'P':
            print("Success")
            return

    # Check for Rooks and Queens (horizontally and vertically)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dr, dc in directions:
        r, c = king_r + dr, king_c + dc
        while 0 <= r < n and 0 <= c < n:
            piece = board[r][c]
            if piece != '.':
                if piece == 'R' or piece == 'Q':
                    print("Success")
                    return
                break
            r += dr
            c += dc

    # Check for Bishops and Queens (diagonally)
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dr, dc in directions:
        r, c = king_r + dr, king_c + dc
        while 0 <= r < n and 0 <= c < n:
            piece = board[r][c]
            if piece != '.':
                if piece == 'B' or piece == 'Q':
                    print("Success")
                    return
                break
            r += dr
            c += dc

    # Check for Knights (although not mentioned in the problem, for completeness
    # and to avoid potential for similar future requests)
    knight_moves = [(king_r - 2, king_c - 1), (king_r - 2, king_c + 1),
                    (king_r - 1, king_c - 2), (king_r - 1, king_c + 2),
                    (king_r + 1, king_c - 2), (king_r + 1, king_c + 2),
                    (king_r + 2, king_c - 1), (king_r + 2, king_c + 1)]
    for nr, nc in knight_moves:
        if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 'N': # Assuming 'N' for Knight
            print("Success")
            return

    print("Fail")

if __name__ == '__main__':
    # Example Test Cases
    board1 = ["........",
              ".P......",
              "........",
              ".....K..",
              "........",
              "........",
              "........",
              "........"]
    is_king_in_check(board1)  # Expected output: Fail

    board2 = ["........",
              "P.......",
              "........",
              ".....K..",
              "........",
              "........",
              "........",
              "........"]
    is_king_in_check(board2)  # Expected output: Success

    board3 = ["........",
              "........",
              "........",
              "Q....K..",
              "........",
              "........",
              "........",
              "........"]
    is_king_in_check(board3)  # Expected output: Success

    board4 = ["........",
              "........",
              "........",
              ".....K.R",
              "........",
              "........",
              "........",
              "........"]
    is_king_in_check(board4)  # Expected output: Success

    board5 = ["........",
              "........",
              ".....B..",
              ".....K..",
              "........",
              "........",
              "........",
              "........"]
    is_king_in_check(board5)  # Expected output: Success

    board6 = ["........",
              "........",
              "........",
              "........",
              "........",
              ".....K..",
              "........",
              "P......."]
    is_king_in_check(board6) # Expected output: Fail

    board7 = ["........",
              "........",
              "........",
              "........",
              "........",
              ".....K..",
              "P.......",
              "........"]
    is_king_in_check(board7) # Expected output: Success

    board8 = ["8x8", # Invalid input, should not crash
              "........",
              "........",
              ".....K..",
              "........",
              "........",
              "........",
              "........"]
    is_king_in_check(board8) # Expected: No output

    board9 = [".......", # Invalid input (not square), should not crash
              "........",
              "........",
              ".....K..",
              "........",
              "........",
              "........",
              "........"]
    is_king_in_check(board9) # Expected: No output

    board10 = ["........",
               "........",
               "........",
               "........",
               "........",
               "........",
               "........",
               "........"]
    is_king_in_check(board10) # Expected: No output (no King)