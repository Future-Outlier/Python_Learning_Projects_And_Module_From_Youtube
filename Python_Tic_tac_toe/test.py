
# todo great function to get
TODO BELOW
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


``

print("random")
tmp = random.choice(locations)
print(tmp[0], tmp[1])


def is_game_over(board):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return True
    return False

def drop_piece(b_copy, row, col, player):
    b_copy[row][col] = player

def score_position(board, player):
