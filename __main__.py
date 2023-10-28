import pygame
from sys import exit
from controller import GameController

def setup_game():
    pygame.init()
    
    screen = pygame.display.set_mode((800, 400))
    clock = pygame.time.Clock()
    pygame.display.set_caption('saveme-game')
    
    game_controller = GameController(game=pygame, screen=screen)
    while True:
        for event in pygame.event.get():
            game_controller.process_event(event=event)

        clock.tick(60)

setup_game()

