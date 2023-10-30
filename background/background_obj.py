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
        return {'surface': surface, 'loc': (x_loc, y_loc)}

    def insert_image(self, file: str, x_loc: int, y_loc: int, width_scale: float = 1, height_scale: float = 1):
        image = self.game.image.load(file)
        scaled_image = self.game.transform.scale(image, (image.get_width() * width_scale, image.get_height() * height_scale))
        self.screen.blit(scaled_image, (x_loc, y_loc))
        return {'surface': scaled_image, 'loc': (x_loc, y_loc)}
