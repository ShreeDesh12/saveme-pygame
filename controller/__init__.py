from .event_process import quit_game

class GameController():
    def __init__(self, game, screen) -> None:
        self.game = game
        self.screen = screen

    def process_event(self, event) -> None:
        if event.type == self.game.QUIT:
            quit_game(game=self.game)

        self.game.display.update()

        

        

