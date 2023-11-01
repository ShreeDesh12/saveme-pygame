import logging
import os
import pygame

image_path = os.path.join(os.getcwd(), 'images/characters')


class Character():
    def __init__(self, name: str, game: pygame, screen, x_loc: int, y_loc: int, file_name: str, position=None) -> None:
        self.name = name
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.game = game
        self.screen = screen
        self.surface = self.game.image.load(os.path.join(image_path, file_name)).convert_alpha()
        surf_postion = (x_loc, y_loc)
        logging.info(surf_postion)
        logging.info(position)
        if position:
            if position.lower() == 'bottom-left':
                surf_postion = self.surface.get_rect(bottomleft=(x_loc, y_loc))

        logging.info(surf_postion)
        self.position = surf_postion
        self.screen.blit(self.surface, surf_postion)
        logging.info(f'Creating character {self.name}')

    def render_character(self):
        self.screen.blit(self.surface, self.position)

    def get_loc(self):
        return self.position
    
    def move(self, new_x_loc: int, new_y_loc: int):
        # logging.info(f'{self.name} moving from {(self.x_loc, self.y_loc)} to {(new_x_loc, new_y_loc)}')
        self.x_loc = new_x_loc
        self.y_loc = new_y_loc
        self.render_character()

    def move_rect(self, right: int = None, left: int = None):
        if not any([right, left]):
            logging.info('right or left not received')
            return
        
        if left:
            self.position.left += left

        if right:
            self.position.right += right
        
        self.render_character()

    def transform(self, width_scale: float, height_scale: float):
        self.surface = self.game.transform.scale(self.surface, (self.surface.get_width() * width_scale, self.surface.get_height() * height_scale))
        self.render_character()
        logging.info(f'Transforming {self.name} by w_scale: {width_scale} | h_scale: {height_scale}')



