import pygame

from background import setup_background
from validator.validator import Validator

from .event_process import quit_game

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

        self.game.display.update()

    def run_clock(self) -> None:
        self.clock.tick(60)
