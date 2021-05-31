import pygame
import sys
from pygame.locals import * # FOR KEYDOWN EVENT !!!
import numpy as np
import math
import random
# for creating the screen board
pygame.init()

STEP = 0
HEIGHT = 600
WIDTH = 600
LINE_WIDTH = 15
SQUARE_SIZE = 200
OFFSET = 55
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
X_LINE_WIDTH = 25
# TODO PLAYER ONE WINS COLORS AND PLAYER TWO WINS COLORS

# FOR FONTS
myfont = pygame.font.SysFont("monospace", 45)
# FOR COLORS
RED = (255, 0, 0)
BG_COLOR = (21, 181, 176)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (249, 189, 192)
CROSS_COLOR = (251, 230, 152)
X_COLOR = (251, 230, 152)
DRAW_COLOR = (109, 236, 224)
# FOR BOARD ROWS AND COLUMNS
BOARD_ROWS = 3
BOARD_COLS = 3

# board
board = np.zeros((BOARD_ROWS, BOARD_COLS))

screen = pygame.display.set_mode( (WIDTH, HEIGHT) ) # for the screen background size
pygame.display.set_caption("TIC TAC TOE")
screen.fill( BG_COLOR ) # the background color
player1 = 1
player2 = 2

def draw_lines():
    # 1 horizontal
    pygame.draw.line( screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH )
    # 2 horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)

    # 1 vertical
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    # 2 vertical
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle( screen, CIRCLE_COLOR, (int( col * 200 + 100), int( row * 200 + 100)), CIRCLE_RADIUS, CIRCLE_WIDTH )
            elif board[row][col] == 2:
                pygame.draw.line(screen, X_COLOR, (col * SQUARE_SIZE + OFFSET, row * SQUARE_SIZE + OFFSET),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - OFFSET, row * SQUARE_SIZE + SQUARE_SIZE - OFFSET),
                                 X_LINE_WIDTH)
                pygame.draw.line(screen, X_COLOR,
                                 (col * SQUARE_SIZE + OFFSET, row * SQUARE_SIZE + SQUARE_SIZE - OFFSET),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - OFFSET, row * SQUARE_SIZE + OFFSET), X_LINE_WIDTH)

def mark_squares(row, col, player): # fill the board by O or X
    board[row][col] = player


def available_square(row, col):
    return board[row][col] == 0 # if 0 means not filled yet

def is_board_full():
    return STEP == 9

def fake_check_win(board, player): # todo don't draw lines
    # 0 means continue 1 means gameover

    # vertical win check
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    # horizontal win check
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    # asc diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True
    # desc diagonal win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    return False

def check_win(board, player): # todo draw lines
    # 0 means continue 1 means gameover
    gameover = 0
    # vertical win check
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            gameover = 1
    # horizontal win check
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            gameover = 1
    # asc diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        gameover = 1
    # desc diagonal win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        gameover = 1

    return gameover == 1


def draw_vertical_winning_line(col, player):
    posX = col * 200 + 100

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line( screen, color, (posX, 15), (posX, HEIGHT - 15), 15 )
def is_game_over(board):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True

def drop_piece(b_copy, row, col, player):
    b_copy[row][col] = player

def get_valid_locations(board):
    locations = []
    for r in range(3):
        for c in range(3):
          if board[r][c] == 0:
              locations.append((r, c))
    return locations




def score_position(board, player):
    score = 0

    ## Score Horizontal
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            score += 10
    ## Score Vertical
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            score += 10
    ## Check negatively sloped diaganols
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        score += 10
    ## Check positively sloped diaganols
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        score += 10

    if player  == player1:
        opp_player = 2
    else:
        opp_player = 1

    # todo if player oop point 3 minus -80
    ## Score Horizontal
    for row in range(BOARD_ROWS):
        if board[row][0] == opp_player and board[row][1] == opp_player and board[row][2] == opp_player:
            score -= 5
    ## Score Vertical
    for col in range(BOARD_COLS):
        if board[0][col] == opp_player and board[1][col] == opp_player and board[2][col] == opp_player:
            score -= 5
    ## Check negatively sloped diaganols
    if board[0][0] == opp_player and board[1][1] == opp_player and board[2][2] == opp_player:
        score -= 5
    ## Check positively sloped diaganols
    if board[0][2] == opp_player and board[1][1] == opp_player and board[2][0] == opp_player:
        score -= 5

    print("player is " + str(player) + " " + "opp_player is " + str(opp_player))
    if score < 0:
        print("opp score "  + str(score) )
    return score

def minimax(board, depth, alpha, beta, maximizingPlayer): # todo False player1 True player2
    valid_locations = get_valid_locations(board) # todo write myself (is ok)
    is_gameover = is_game_over(board) # todo write nested loop myself
    # todo the ai first step put middle
    empty = 0
    middle = board[1][1]
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                empty += 1
    if empty == 8 and middle == 2:
        return 1, 1, 100000000
    if depth == 0 or is_gameover:
        if is_gameover:
            print("is_gameover error")
            if fake_check_win(board, player2):# todo AI_PIECE to player2
                print("error 1")
                return (None, None, 10000000000000)
            elif fake_check_win(board, player1): # todo PLAYER_PIECE to player1
                print("error 2")
                return (None, None, -10000000000000)
            else: # Game is over, no more valid moves
                print("error 3")
                return (None, None, 0)
        else: # Depth is zero
            print("error 4")
            return (None, None, score_position(board, player2)) # todo figure why wrote like this

    if maximizingPlayer:
        value = -math.inf

        if valid_locations != None:
            tmp = random.choice(valid_locations)
            ans_row = tmp[0]
            ans_col = tmp[1]
            # todo below drop piece
            for square in valid_locations:
                row = square[0] # todo so we have valid locations and just go through it
                col = square[1]
                b_copy = board.copy() # todo important so that we don't affect the original board.
                drop_piece(b_copy, row, col, player2)
                new_score = minimax(b_copy, depth - 1, alpha, beta, False)[2] # get the score_position when depth is zero
                if new_score > value:
                    value = new_score
                    ans_col  = col
                    ans_row = row
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return ans_row, ans_col, value
        else:
            return None, None, value

    else: # Minimizing player
        value = math.inf  # infinity numbers

        if valid_locations != None:
            tmp = random.choice(valid_locations)
            ans_row = tmp[0]
            ans_col = tmp[1]
            for square in valid_locations:
                row = square[0]  # todo so we have valid locations and just go through it
                col = square[1]
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
            return ans_row, ans_col, value
        else:
            return None, None, value



def draw_horizontal_winning_line(row, player):
    posY = row * 200 + 100

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), 15)

def draw_asc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line( screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15 )

def draw_desc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)

def restart():
    screen.fill(BG_COLOR)  # the background color
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0





player = 1
game_over = False
draw_lines()
step = 0
# main loop
while True:
    if step == 9 and not game_over:
        label = myfont.render("DRAW", 1, DRAW_COLOR)
        screen.blit(label, (250, 200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                step = 0
                game_over = False
                restart()

        if  player == 1 and event.type == pygame.MOUSEBUTTONDOWN and not game_over and step != 9:
            mouseX = event.pos[0] # x
            mouseY = event.pos[1] # y

            clicked_col = int(mouseX // 200)
            clicked_row = int(mouseY // 200)

            if available_square( clicked_row, clicked_col ):
                step += 1
                if player == 1:
                    mark_squares( clicked_row, clicked_col, 1)
                    if check_win(board, player):
                        game_over = True
                        label = myfont.render("Player 1 wins!!", 1, CIRCLE_COLOR)
                        screen.blit(label, (100, 200))
                    player = 2

    if step == 9 and not game_over:
        label = myfont.render("DRAW", 1, DRAW_COLOR)
        screen.blit(label, (250, 200))
    if player == 2 and not game_over and step != 9:
        print(step)
        # col = random.randint(0, COLUMN_COUNT-1)
        #col = pick_best_move(board, AI_PIECE)
        row, col, minimax_score = minimax(board, 4, -math.inf, math.inf, True)
        print(row, col, minimax_score)
        if available_square(row, col):
            step += 1
            pygame.time.wait(500)
            mark_squares( row, col, 2)

            if check_win(board, player):
                game_over = True
                label = myfont.render("AI wins!!", 1, CROSS_COLOR)
                screen.blit(label, (200, 200))
            player = 1



    draw_figures()
    pygame.display.update()




