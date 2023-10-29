import logging
import pygame
from validator.validator import Validator

class BackgroundController():
    def __init__(self, game: pygame, screen) -> None:
        self.game = game
        self.screen = screen
        self.validator = Validator(game=game)

    def create_line(self, x_loc=0, y_loc=0, pixel_length=5, pixel_width=10, color='White') -> None:
        self.validator.validate_surface(x_loc=x_loc, y_loc=y_loc)
        
        surface = self.game.Surface((pixel_length, pixel_width))
        surface.fill(color)
        self.screen.blit(surface, (x_loc, y_loc))
        logging.info('Line created')
