import logging
import pygame
import traceback

from .background_obj import *

def setup_background(game: pygame, screen) -> dict:

    try:
        background_controller = BackgroundController(game=game, screen=screen)
        background_controller.create_line(x_loc=700, y_loc=20, pixel_width=160)

    except Exception as e:
        logging.exception(e)
        logging.info(traceback.format_exc())
        return {'error': 'Crashing in background setup'}
    
    return {'message': 'success'}