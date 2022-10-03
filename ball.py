import pygame as pg
import random
import time
from settings import *


class Ball:
    def __init__(self, game, paddle, opponent):
        self.game = game
        self.paddle = paddle
        self.opponent = opponent
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.radius = 10
        self.speed_x = 3
        self.speed_y = 3
        self.acceleration = 1.0
        self.color = 'white'
    

    def draw(self):
        pg.draw.circle(self.game.screen, self.color,(self.x, self.y), self.radius)
    

    def update(self):
        self.x += self.speed_x  * self.acceleration
        self.y += self.speed_y * self.acceleration

        self.map_collision()
        self.player_collision()
        self.opponent_collision()


    def map_collision(self):
        if self.y - self.radius < 0:
            self.speed_y = -self.speed_y
        
        if self.y + self.radius > HEIGHT:
            self.speed_y = -self.speed_y


    def player_collision(self):      
        if self.x - self.radius / 2 < self.paddle.x + self.paddle.width:
            self.speed_x = -self.speed_x
            self.acceleration += 0.05

        if self.x < 0:
            self.game.opponent_score += 1
            self.reset()


    def opponent_collision(self):
        if self.x + self.radius / 2 > self.opponent.x and self.y > self.opponent.y and self.y < self.opponent.y + self.opponent.height:
            self.speed_x = -self.speed_x
            self.acceleration += 0.05

        if self.x + self.radius > WIDTH :
            self.game.player_score += 1
            self.reset()


    def reset(self):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2

        self.speed_x = random.choice([-3, 3])
        self.speed_y = random.choice([-3, 3])
        self.acceleration = 1

        self.paddle.y = self.opponent.y = HEIGHT / 2 - self.paddle.height / 2
        time.sleep(1)

