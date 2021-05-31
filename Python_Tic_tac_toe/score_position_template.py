def score_position(board, player):
    score = 0
    # todo below i don't know

    # todo warniing maybe slope need to be notice
    ## Score Horizontal
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            score += 100
    ## Score Vertical
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            score += 100
    ## Check negatively sloped diaganols
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        score += 100
    ## Check positively sloped diaganols
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        score += 100

    if score == 0 and board[0][0]:
        score += 50

    return score