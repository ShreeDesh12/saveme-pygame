import logging
import pygame
from sys import exit
from controller import GameController

def setup_logger():
    logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logging.warning('Logger started')

def setup_game():
    pygame.init()
    
    game_controller = GameController(game=pygame)
    game_controller.setup()
    while True:
        for event in pygame.event.get():
            game_controller.process_event(event=event)

        game_controller.run_clock()


setup_logger()
setup_game()

