

def winning_move(board, piece):
    # Check horizontal locations for win
    # every possibility horizontal 4 in the board
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece\
                    and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece \
                    and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT-3): # 4 * 3 kinds of possibility
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece \
                    and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diagnols
    for c in range(COLUMN_COUNT-3): # 4 * 3 kinds of possibility
        for r in range(3,ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece \
                    and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True


        True