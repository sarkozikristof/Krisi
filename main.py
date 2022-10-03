import pygame as pg
from settings import *
from paddle import *
from ball import *
from opponent import *
from board import *


class Game:
    def __init__(self):
        pg.init()
        self.player_score = 0
        self.opponent_score = 0
        self.screen = pg.display.set_mode(RESOLUTION)
        self.clock = pg.time.Clock()
        self.new_game()


    def new_game(self):
        self.paddle = Paddle(self)
        self.opponent = Opponent(self)
        self.ball = Ball(self, self.paddle, self.opponent)
        self.board = Board(self)


    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f'{abs(self.ball.speed_x) :.1f}')
        self.paddle.update()
        self.opponent.update()
        self.ball.update()


    def draw(self):
        self.screen.fill('black')
        self.paddle.draw()
        self.opponent.draw()
        self.ball.draw()
        self.board.draw()


    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()


    def run(self):
        while True:
            self.check_events()
            self.draw()
            self.update()



if __name__ == '__main__':
    game = Game()
    game.run()