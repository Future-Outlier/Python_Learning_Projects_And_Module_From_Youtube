import numpy as np
import pygame
import sys
import math

BLUE =  (21, 215, 234) #　TODO THE FENCE OF THE BOARD
BLACK = (0,0,0)
RED =  (255,128,114)
YELLOW =  (21, 234, 147) # 255,128,114　 TODO ONE OF THE PIECE
GREEN =  (227, 234, 21) # TODO ONE OF THE PIECE
ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

# All we need to do is make sure the top row of the specific column is zero.
def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0: # return the first empty row.
            return r

def print_board(board): # to see the board from button up
    print(np.flip(board, 0)) # todo look the reference.

def winning_move(board, piece):
    # Check horizontal locations for win
    # every possibility horizontal 4 in the board
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT-3): # 4 * 3 kinds of possibility
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diagnols
    for c in range(COLUMN_COUNT - 3):  # 4 * 3 kinds of possibility
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and \
                    board[r - 3][c + 3] == piece:
                return True

def draw_board(board): # RECT AND CIRCLE THE IMPORTANT PART IS THE CENTER.
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT): # r+1 means the toppest we don't want to be blue
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, (r+1)*SQUARESIZE, SQUARESIZE, SQUARESIZE))#TODO put the reference  pygame.draw.rect
            #if board[r][c] == 0:
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, GREEN, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)

    pygame.display.update()

board = create_board()
game_over = False
turn = 0

pygame.init() # todo look docs

SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE #An additional row to put the circles dropping.

size = (width,height) # tuple

RADIUS = int(SQUARESIZE/2 - 5) # To be not radius

screen = pygame.display.set_mode(size) # todo look docs
draw_board(board)
pygame.display.update()


myfont = pygame.font.SysFont("monospace", 75)

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE)) # TODO SEE THE DOCS
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, GREEN, (posx, int(SQUARESIZE/2)), RADIUS)
            elif turn == 1:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            #print(event.pos)
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE)) # To clean the draw circle at the end of the game.
            # Ask for Player 1 Input
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if winning_move(board, 1):
                        label = myfont.render("Player 1 wins!!", 1, GREEN)
                        screen.blit(label, (40,10))
                        game_over = True

            # Ask for Player 2 Input
            else:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if winning_move(board, 2):
                        label = myfont.render("Player 2 wins!!", 1, YELLOW)
                        screen.blit(label, (40, 10))
                        game_over = True

            print_board(board)
            draw_board(board)
            # Take turnsx
            turn += 1
            turn %= 2
            if game_over:
                pygame.time.wait(30000000) # 3000ms
