import logging
import pygame
import os

from background import setup_background
from validator.validator import Validator

from .event_process import quit_game

dir_path = os.getcwd()
image_path = os.path.join(dir_path, 'images')

characters = {}
def setup_characters(game: pygame, screen):
    enemy = Character(name='enemy', game=game, screen=screen, x_loc=700, y_loc=230, file_name='characters\elephant.png')
    # enemy.transform(width_scale=4, height_scale=4)
    characters['enemy'] = enemy


class GameController():
    def __init__(self, game: pygame) -> None:
        self.game = game
        self.screen = None
        self.clock = None
        self.validator = Validator(game=game)
        self.surfaces = list()

    def _setup_display(self) -> None:
        setup_response = setup_background(game=self.game, screen=self.screen)
        if 'error' in setup_response:
            logging.error(f'Error in setup response: {setup_response}')
            self.game.quit()
        self.surfaces = setup_response.get('surfaces')

        setup_characters(game=self.game, screen=self. screen)

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

    def run_game(self):
        for surface_details in self.surfaces:
            self.screen.blit(surface_details.get('surface'), surface_details.get('loc'))

        enemy = characters['enemy']
        x_loc, y_loc = enemy.get_loc()
        enemy.move(x_loc-1, y_loc)
        self.game.display.update()

    def run_clock(self) -> None:
        self.clock.tick(60)


class Character():
    def __init__(self, name: str, game: pygame, screen, x_loc: int, y_loc: int, file_name: str) -> None:
        self.name = name
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.game = game
        self.screen = screen
        self.surface = self.game.image.load(os.path.join(image_path, file_name))
        self.screen.blit(self.surface, (x_loc, y_loc))
        logging.info(f'Creating character {self.name}')

    def render_character(self):
        self.screen.blit(self.surface, (self.x_loc, self.y_loc))

    def get_loc(self):
        return (self.x_loc, self.y_loc)
    
    def move(self, new_x_loc: int, new_y_loc: int):
        # logging.info(f'{self.name} moving from {(self.x_loc, self.y_loc)} to {(new_x_loc, new_y_loc)}')
        self.x_loc = new_x_loc
        self.y_loc = new_y_loc
        self.render_character()

    def transform(self, width_scale: float, height_scale: float):
        self.surface = self.game.transform.scale(self.surface, (self.surface.get_width() * width_scale, self.surface.get_height() * height_scale))
        self.render_character()
        logging.info(f'Transforming {self.name} by w_scale: {width_scale} | h_scale: {height_scale}')



