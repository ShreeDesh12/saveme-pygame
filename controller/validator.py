import pygame

class Validator():
    def __init__(self, game: pygame) -> None:
        self.game = game
    
    def validate_surface(self, x_loc: int, y_loc: int):
        x_loc = int(x_loc)
        y_loc = int(y_loc)
