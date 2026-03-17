from enum import show_flag_values
from typing import List
import pygame
from main import boardSize
from main import board

class Pawn:
    isSelected = False

    def __init__(self, waypath: bool, board_positon_x: int, board_positon_y: int, board: List):
        self.waypath = waypath
        self.position = {"x": board_positon_x, "y": board_positon_y }

        boardPos = board[self.position['x']][self.position['y']]
        gen_size = boardSize['size']
        self.rect = pygame.Rect(boardPos[0], boardPos[1], gen_size, gen_size)
        self.mainBoard = board

    def show_possible_moves(self, screen):
        gen_size = boardSize['size']
        pos_forward = self.mainBoard[self.position['x']][self.position['y'] - 1]
        rect_forward = pygame.Rect(pos_forward[0], pos_forward[1], gen_size, gen_size)
        pygame.draw.rect(screen, "green", rect_forward)
    
    def display(self, screen, pawn_surface):
        boardPos = self.mainBoard[self.position['x']][self.position['y']]
        gen_size = boardSize['size']
        mainRect = pygame.Rect(boardPos[0], boardPos[1], gen_size, gen_size)

        pygame.draw.rect(screen, "red", mainRect)
        resized_pawn = pygame.transform.scale(pawn_surface, (gen_size, gen_size))
        screen.blit(resized_pawn, mainRect)

        if self.isSelected:
            self.show_possible_moves(screen)
