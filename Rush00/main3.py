#!/usr/bin/env python3

def checkmate(board):
    if not isinstance(board, list):
        return "Error: Invalid input"  # Or return None, or raise an exception

    if not board:
        return "Error: Empty board"

    king_row, king_col = -1, -1
    for r, row in enumerate(board):
        if not isinstance(row, str):
            return "Error: Invalid board row type"
        for c, cell in enumerate(row):
            if cell == 'K':
                king_row, king_col = r, c
                break
        if king_row != -1:
            break

    if king_row == -1:
        return "Error: King not found on the board"

    rows = len(board)
    cols = len(board[0]) if rows > 0 else 0  # Handle empty board case

    def is_valid_move(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def check_pawn(r, c):
        # Pawns attack diagonally one square forward
        attack_dirs = [(r - 1, c - 1), (r - 1, c + 1)]  # Assuming opponent's pawns
        for ar, ac in attack_dirs:
            if is_valid_move(ar, ac) and board[ar][ac] == 'P':
                return True
        return False

    def check_rook(r, c):
        # Rooks attack horizontally and vertically
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            cr, cc = r + dr, c + dc
            while is_valid_move(cr, cc):
                if board[cr][cc] != '.':
                    if board[cr][cc] == 'R':
                        return True
                    else:
                        break  # Piece is blocking
                cr, cc = cr + dr, cc + dc
        return False

    def check_bishop(r, c):
        # Bishops attack diagonally
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dr, dc in directions:
            cr, cc = r + dr, c + dc
            while is_valid_move(cr, cc):
                if board[cr][cc] != '.':
                    if board[cr][cc] == 'B':
                        return True
                    else:
                        break  # Piece is blocking
                cr, cc = cr + dr, cc + dc
        return False

    def check_queen(r, c):
        # Queen attacks horizontally, vertically, and diagonally
        return check_rook(r, c) or check_bishop(r, c)

    # Check for attacks
    if check_pawn(king_row, king_col) or \
       check_rook(king_row, king_col) or \
       check_bishop(king_row, king_col) or \
       check_queen(king_row, king_col):
        return "Success"
    else:
        return "Fail"


if __name__ == "__main__":
    # Example 1
    board1 = [
        "........",
        "....P...",
        "......B.",
        ".....K..",
        "........",
        "........",
        "........",
        "........",
    ]
    print(checkmate(board1))

    # Example 2
    board2 = [
        ".......R",
        "........",
        "........",
        ".....K..",
        "........",
        "........",
        "........",
        "........",
    ]
    print(checkmate(board2))

    # Example 3
    board3 = ["K.....",
              "......Q",
              ".......",
              ".......",
              ".......",
              ".......",
              ".......",
              "......."]
    print(checkmate(board3))

    # Example 4 (Fail)
    board4 = ["K.....",
              ".......",
              ".......",
              ".......",
              ".......",
              ".......",
              ".......",
              "......."]
    print(checkmate(board4))

    # Example 5 (Error - Invalid Input)
    board5 = "Invalid"
    print(checkmate(board5))

    # Example 6 (Error - Empty Board)
    board6 = []
    print(checkmate(board6))
    
    # Example 7 (Pawn Check)
    board7 = [
        "........",
        "P.......",
        "........",
        "K.......",
        "........",
        "........",
        "........",
        "........",
    ]
    print(checkmate(board7))