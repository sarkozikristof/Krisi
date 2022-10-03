import pygame as pg
from settings import *


class Board:
    def __init__(self, game):
        self.game = game
        self.color = 'white'
    

    def draw(self):
        pg.draw.aaline(self.game.screen, self.color, (WIDTH / 2, 0), (WIDTH / 2, HEIGHT))

        self.player_score()
        self.opponent_score()


    def player_score(self):
        myFont = pg.font.SysFont("Times New Roman", 40)
        player_text = myFont.render(f'{self.game.player_score}', False, 'white')
        self.game.screen.blit(player_text, (WIDTH / 2 - 50, HEIGHT / 2))


    def opponent_score(self):
        myFont = pg.font.SysFont("Times New Roman", 40)
        player_text = myFont.render(f'{self.game.opponent_score}', False, 'white')
        self.game.screen.blit(player_text, (WIDTH / 2 + 30, HEIGHT / 2))
