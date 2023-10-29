import pygame
import os

from background import setup_background
from validator.validator import Validator

from .event_process import quit_game

dir_path = os.getcwd()

class GameController():
    def __init__(self, game: pygame) -> None:
        self.game = game
        self.screen = None
        self.clock = None
        self.validator = Validator(game=game)

    def _setup_display(self) -> None:
        setup_background(game=self.game, screen=self.screen)

    def setup(self) -> None:
        self.screen = self.game.display.set_mode((800, 400))
        self.clock = self.game.time.Clock()
        self.game.display.set_caption('saveme-game')
        self._setup_display()

    def process_event(self, event: pygame.event) -> None:
        if event.type == self.game.QUIT:
            quit_game(game=self.game)
        else:
            pass

        self.game.display.update()

    def run_game(self):
        enemy = self.game.image.load(os.path.join(dir_path, 'images\characters\woman-1.jpg'))
        enemy = self.game.transform.scale(enemy, (enemy.get_width() * 1/80, enemy.get_height() * 1/80))
        
        self.screen.blit(enemy, (700, 270))

    def run_clock(self) -> None:
        self.clock.tick(60)


class Character():
    def __init__(self, game, x_loc, y_loc, file_name) -> None:
        self.x_loc = 0
        self.y_loc = 0
        self.game = game
        self.surface = self.game.image.load(os.path.join(dir_path, 'images\characters\woman-1.jpg'))