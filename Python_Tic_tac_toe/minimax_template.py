def is_game_over(board):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return True
    return False

def drop_piece(b_copy, row, col, player):
    b_copy[row][col] = player

 def get_valid_locations(board):
     import numpy as np
     import random
     locations = []

     board = np.zeros((3, 3))
     for r in range(3):
         for c in range(3):
             if board[r][c] == 0:
                 locations.append((r, c))

     for i in range(len(locations)):
         print(locations[i][0], locations[i][1])

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

def minimax(board, depth, alpha, beta, maximizingPlayer): # todo False player1 True player2
    valid_locations = get_valid_locations(board) # todo write myself (is ok)
    is_gameover = is_game_over(board) # todo write nested loop myself
    if depth == 0 or is_gameover:
        if is_gameover:
            if winning_move(board, player2):# todo AI_PIECE to player2
                return (None, None, 10000000000000)
            elif winning_move(board, player1): # todo PLAYER_PIECE to player1
                return (None, None, -10000000000000)
            else: # Game is over, no more valid moves
                return (None, None, 0)
        else: # Depth is zero
                return (None, None, score_position(board, player2)) # todo figure why wrote like this

    if maximizingPlayer:
        value = -math.inf
        tmp = random.choice(valid_locations)
        ans_row = tmp[0], ans_col = tmp[1]
        # todo below drop piece
        for i in range(len(valid_locations)):
            row = valid_locations[i][0] # todo so we have valid locations and just go through it
            col = valid_locations[i][1]
            b_copy = board.copy() # todo important so that we don't affect the original board.
            drop_piece(b_copy, row, col, player2)
            new_score = minimax(b_copy, depth - 1, alpha, beta, False)[2] # get the score_position when depth is zero
            if new_score > value:
                value = new_score
                ans_col  = col
                ans_row = row
            alpha = max(alpha, value)
            if alpha >= beta:
                break;
        return row, column, value

    else: # Minimizing player
        value = math.inf  # infinity numbers
        column = random.choice(valid_locations) # todo we change the statement to tictactoe version
        for i in range(len(valid_locations)):
            row = valid_locations[i][0]  # todo so we have valid locations and just go through it
            col = valid_locations[i][1]
            b_copy = board.copy()
            drop_piece(b_copy, row, col, player1)
            new_score = minimax(b_copy, depth-1, alpha, beta, True)[2]
            if new_score < value:
                value = new_score
                ans_col = col
                ans_row = row
            beta = min(beta, value)
            if alpha >= beta:
                break
        return row, column, value


