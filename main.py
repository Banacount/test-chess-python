import os
import pygame

pygame.init()
scrSize = (1280, 720)
mainFps = 60
screen = pygame.display.set_mode(scrSize, pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.display.set_caption("Chess dumbass")


# Global variables
isRunning = True
boardSize = {'rows': 8, 'cols': 8, 'size': 50}
board = [[0 for _ in range(boardSize['rows'])] for _ in range(boardSize['cols'])]


# Colors
colors = {
    'bg-1': pygame.Color(207, 131, 112),
    'white': pygame.Color(238, 238, 238),
    'black': pygame.Color(48, 48, 48),
}


# Load images
pawn_path = os.path.join('ass', 'pawn_chessting.png')
pawn_surface = None

# Load surfaces of images
try:
    pawn_surface = pygame.image.load(pawn_path).convert_alpha()
except pygame.error as err:
    print(f"Cannot load this image: '{err}'")
    exit()


# Main loop
def main():
    global isRunning
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

        screen.fill(colors['bg-1'])
        renderBoard(boardPos['x'], boardPos['y'])

        # test field
        testRect = pygame.Rect(20, 20, 50, 50)
        pygame.draw.rect(screen, "red", testRect)
        resized_pawn = pygame.transform.scale(pawn_surface, (50, 50))
        screen.blit(resized_pawn, testRect)

        pygame.display.flip()
        clock.tick(mainFps)
    pygame.quit()


# Functions
# Create board function
def renderBoard(board_offset_x, board_offset_y):
    stack_x, stack_y = 0, 0

    blackFirst = True
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

        blackFirst = not blackFirst
        stack_y += boardSize['size']


# Execute guard
if __name__ == "__main__":
    main()
