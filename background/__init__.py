import logging
import os
import pygame
import traceback

from .background_obj import *

def setup_background(game: pygame, screen) -> dict:
    dir_path = os.getcwd()
    all_surfaces = []

    try:
        background_controller = BackgroundController(game=game, screen=screen)
        line = background_controller.create_line(x_loc=700, y_loc=20, pixel_width=160)
        img1 = background_controller.insert_image(file=os.path.join(dir_path, 'background\images\dessert.jpg'), 
                                                  x_loc=0, y_loc=0, 
                                                  width_scale=1/7, height_scale=1/10)
        all_surfaces.append(line)
        all_surfaces.append(img1)

    except Exception as e:
        logging.exception(e)
        logging.info(traceback.format_exc())
        return {'error': 'Crashing in background setup'}
    
    return {'message': 'success', 'surfaces': all_surfaces}