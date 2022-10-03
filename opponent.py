import pygame as pg
from settings import *


class Opponent:
    def __init__(self, game):
        self.game = game
        self.height = HEIGHT / 5
        self.width = WIDTH / 75
        self.x = WIDTH - WIDTH / 60
        self.y = HEIGHT / 2 - self.height / 2
        self.color = 'white'
        self.speed = 5


    def draw(self):
        pg.draw.rect(self.game.screen, self.color, (self.x, self.y, self.width, self.height))
    

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_DOWN]:
            self.y += self.speed
        if keys[pg.K_UP]:
            self.y += -self.speed
        
        self.check_movement()


    def check_movement(self):
        if self.y < 0:
            self.y = 0
        if self.y + self.height > HEIGHT:
            self.y = HEIGHT - self.height 