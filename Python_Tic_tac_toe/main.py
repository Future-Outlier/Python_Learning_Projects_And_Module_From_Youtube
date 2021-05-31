import pygame, sys
from pygame.locals import * # FOR KEYDOWN EVENT !!!
import numpy as np
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

def check_win(player):
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
                player = 1
                game_over = False
                restart()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0] # x
            mouseY = event.pos[1] # y

            clicked_col = int(mouseX // 200)
            clicked_row = int(mouseY // 200)

            if available_square( clicked_row, clicked_col ):
                step += 1
                if player == 1:
                    mark_squares( clicked_row, clicked_col, 1)
                    if check_win(player):
                        game_over = True
                        label = myfont.render("Player 1 wins!!", 1, CIRCLE_COLOR)
                        screen.blit(label, (100, 200))
                    player = 2
                elif player == 2:
                    mark_squares( clicked_row, clicked_col, 2)
                    if check_win(player):
                        game_over = True
                        label = myfont.render("Player 2 wins!!", 1, CROSS_COLOR)
                        screen.blit(label, (100, 200))
                    player = 1


    draw_figures()
    pygame.display.update()




