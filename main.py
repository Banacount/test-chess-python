import os
import pygame
from colors import colors
import pieces

pygame.init()
scrSize = (1280, 720)
mainFps = 60
screen = pygame.display.set_mode(scrSize, pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.display.set_caption("Chess dumbass")

# Global variables
isRunning = True
boardSize = {'rows': 8, 'cols': 8, 'size': 50}
allPiecesRect = [] # list of all pieces to track collision

# Board layout [row][column]
board = [[[0, 0] for _ in range(boardSize['rows'])] for _ in range(boardSize['cols'])]

# Load images
pawn_path = os.path.join('ass', 'pawn_chessting.png')

# Load surfaces of images
try:
    pawn_surface = pygame.image.load(pawn_path).convert_alpha()
except pygame.error as err:
    print(f"Cannot load this image: '{err}'")
    exit()


# Main loop
def main():
    global isRunning

    # Local no loop variables
    testpawn1_toggle = False
    allPiecesRect.append(pygame.Rect(0, 0, 0, 0))
    while isRunning:
        scrCenter = screen.get_size()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False

        # Controls
        key_pressed = pygame.key.get_pressed()
        # Esc exit (for development purpuses)
        if key_pressed[pygame.K_ESCAPE]:
            print("Goodbyes!")
            isRunning = False

        # Calculate board size to be centered
        boardPos = {
            'x': (scrCenter[0] / 2) - ((boardSize['size'] * boardSize['cols']) / 2),
            'y': (scrCenter[1] / 2) - ((boardSize['size'] * boardSize['rows']) / 2)
        }

        # DISPLAY METHODS
        screen.fill(colors['bg-1'])
        renderBoard(boardPos['x'], boardPos['y'])

        pawn_test = pieces.Pawn(False, 3, 7, board)
        allPiecesRect[0] = pawn_test.rect
        pawn_test.isSelected = testpawn1_toggle
        pawn_test.display(screen, pawn_surface)

        pygame.display.flip()
        clock.tick(mainFps)

        ms_x, ms_y = pygame.mouse.get_pos()
        if allPiecesRect[0].collidepoint(ms_x, ms_y) and pygame.mouse.get_just_pressed()[0]:
            testpawn1_toggle = not testpawn1_toggle

    pygame.quit()


# Functions
# Create board function
def renderBoard(board_offset_x, board_offset_y):
    stack_x, stack_y = 0, 0

    blackFirst = True
    global board
    for c, row in enumerate(board):
        stack_x = 0
        color_switch = blackFirst

        for i, col in enumerate(row):
            tempRect = pygame.Rect(board_offset_x + stack_x,
                                   board_offset_y + stack_y,
                                   boardSize['size'],
                                   boardSize['size'])

            if color_switch:
                pygame.draw.rect(screen, colors['black'], tempRect)
            else:
                pygame.draw.rect(screen, colors['white'], tempRect)

            color_switch = not color_switch
            stack_x += boardSize['size']
            board[i][c] = [tempRect.x, tempRect.y]

        blackFirst = not blackFirst
        stack_y += boardSize['size']


# Execute guard
if __name__ == "__main__":
    main()
    print(board)
