import logging
import pygame
import os

from background import setup_background
from background.characters import setup_characters
from validator.validator import Validator

from .event_process import quit_game

dir_path = os.getcwd()


class GameController():
    def __init__(self, game: pygame) -> None:
        self.game = game
        self.screen = None
        self.clock = None
        self.validator = Validator(game=game)
        self.surfaces = list()
        self.characters = dict()
        self.title = ''

    def _setup_display(self) -> None:
        setup_response = setup_background(game=self.game, screen=self.screen)
        if 'error' in setup_response:
            logging.error(f'Error in setup response: {setup_response}')
            self.game.quit()
        self.surfaces = setup_response.get('surfaces') or []

        self.characters = setup_characters(game=self.game, screen=self. screen)

    def setup(self) -> None:
        self.screen = self.game.display.set_mode((800, 400))
        self.clock = self.game.time.Clock()
        self.game.display.set_caption('saveme-game')
        self.font = self.game.font.Font(None, 42)
        self.title = self.font.render('My game', False, 'Black')
        self._setup_display()

    def process_event(self, event: pygame.event) -> None:
        if event.type == self.game.QUIT:
            quit_game(game=self.game)
        else:
            pass

    def run_game(self):

        for surface_details in self.surfaces:
            self.screen.blit(surface_details.get('surface'), surface_details.get('loc'))

        enemy = self.characters.get('enemy')
        if enemy:
            position = enemy.get_loc()
            if isinstance(position, tuple):
                x_loc, y_loc = position
                # logging.info(f'{x_loc}, {y_loc}')
                x_loc = 850 if x_loc < -50 else x_loc
                enemy.move(x_loc-4, y_loc)
            
            else:
                enemy.move_rect(right=-2)

        self.screen.blit(self.title, (350, 50))
        self.game.display.update()

    def run_clock(self) -> None:
        self.clock.tick(60)
