import pygame as pg
from settings import *


class Board:
    def __init__(self, game):
        self.game = game
        self.color = 'white'
    
    def draw(self):
        pg.draw.aaline(self.game.screen, self.color, (WIDTH / 2, 0), (WIDTH / 2, HEIGHT))

    def update(self):    
        self.player_score()
        self.opponent_score()

    def player_score(self):
        myFont = pg.font.SysFont("Times New Roman", 18)
        NumLabel = myFont.render(str(self.game.player_score), 1, 'black')
        self.game.screen.blit(NumLabel, (100, 100))    

    def opponent_score(self):
        pass
