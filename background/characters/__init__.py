import pygame

from .models import Character

def setup_characters(game: pygame, screen) -> dict:
    characters = {}
    enemy = Character(name='enemy', game=game, screen=screen, x_loc=700, y_loc=350, file_name='elephant.png', position='bottom-left')
    # enemy.transform(width_scale=4, height_scale=4)
    characters['enemy'] = enemy
    return characters