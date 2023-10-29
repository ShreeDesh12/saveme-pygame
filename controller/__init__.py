import pygame
from .event_process import quit_game
from .validator import Validator

class GameController():
    def __init__(self, game: pygame) -> None:
        self.game = game
        self.screen = None
        self.clock = None
        self.validator = Validator(game=game)

    def _add_surface(self, x_loc: int=0, y_loc: int=0, pixel_length: int=0, pixel_width: int=0, color: str='Red') -> None:
        self.validator.validate_surface(x_loc=x_loc, y_loc=y_loc)
        surface = self.game.Surface((pixel_length, pixel_width))
        surface.fill(color)
        self.screen.blit(surface, (x_loc, y_loc))

    def _setup_display(self) -> None:
        self._add_surface(x_loc=-700, y_loc=10, pixel_length=5, pixel_width=380)

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
